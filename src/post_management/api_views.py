from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer, RankItemSerializer
from .models import Post, RankItem


def serializePostByID(post_id):
    post = Post.objects.get(id=post_id)
    post_serializer = PostSerializer(post)

    rank_item_queryset = RankItem.objects.filter(post=post)
    rank_item_serializer = RankItemSerializer(rank_item_queryset, many=True)

    return {
        **post_serializer.data,
        "rank_list": rank_item_serializer.data
    }


@api_view(['GET'])
def getPostByID(request, post_id):
    
    if not Post.objects.filter(id=post_id).exists():
        return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializePostByID(post_id), status=status.HTTP_200_OK)

@api_view(['POST'])
def createPost(request):

    post_data = request.data

    # extract rank list from post data
    rank_list = post_data.pop('rank_list')

    post_serializer = PostSerializer(data=post_data)
    post_serializer.is_valid(raise_exception=True)

    rank_serializer = RankItemSerializer(data=rank_list, many=True)
    rank_serializer.is_valid(raise_exception=True)

    # check if the rank list has exactly 10 items
    if len(rank_serializer.validated_data) != 10:
        return Response({"detail": "Rank items in the list must be 10"}, status=status.HTTP_400_BAD_REQUEST)
    
    # if the post data and rank item is valid, save the post and rank items
    # overwrite the modify_user field with the current user
    post_serializer.modify_user = request.user.id
    post = post_serializer.save()
    for rank_item in rank_serializer.validated_data:
        RankItem.objects.create(post=post, **rank_item)

    print(post.id)

    return Response(serializePostByID(post.id), status=status.HTTP_200_OK)


@api_view(['PUT'])
def updatePost(request, post_id):
    post_data = request.data

    # extract rank list from post data
    rank_list = post_data.pop('rank_list')

    post = Post.objects.get(id=post_id)
    post_serializer = PostSerializer(instance=post, data=post_data)
    post_serializer.is_valid(raise_exception=True)


    bulk_update_rank_items = []

    # accpet partial update for rank item list,
    # but creating new rank items is not allowed
    for idx, modifying_rank_item in enumerate(rank_list):
        try:
            rank_item = RankItem.objects.get(id=modifying_rank_item['id'])
        except RankItem.DoesNotExist:
            return Response({"detail": f"The {idx+1} Rank item ID ({modifying_rank_item['id']}) does not match any instance in DB"}, status=status.HTTP_404_NOT_FOUND)
        rank_item_serializer = RankItemSerializer(instance=rank_item, data=modifying_rank_item)
        rank_item_serializer.is_valid(raise_exception=True)
        
        bulk_update_rank_items.append(rank_item_serializer)

    
    # if the post data and rank item data is valid, save the post and rank items
    # overwrite the modify_user field with the current user
    post_serializer.modify_user = request.user.id
    post_serializer.save()
    for rank_item in bulk_update_rank_items:
        rank_item.save()

    return Response(serializePostByID(post.id), status=status.HTTP_200_OK)


@api_view(['DELETE'])
def deletePost(request, post_id):

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
    # delete the post and cascade delete the rank items
    post.delete()

    return Response({"detail": "Post deleted"}, status=status.HTTP_200_OK)