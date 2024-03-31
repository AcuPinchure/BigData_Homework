# Introduction

This repository is a demo project for BigData company interview.

The Goal of this project is to create a simplfied replica CRUD API for posts on [DailyViewTW website](https://dailyview.tw/).


# API Documentation
There are 4 APIs in `post_management` app:
- [create a post](#create-a-post)
- [retrieve a post by ID](#retrieve-a-post-by-id)
- [update a post by ID](#update-a-post-by-id)
- [delete a post by ID](#delete-a-post-by-id)

## Create a Post
### URL
```
POST /PM/api/post/create/
```
### Authorization Type
Include the JWT Token in the request Header
```
Authorization: Bearer <JWT Token>
```
### Request Body
The complete post data, with 3 parts, requests with any of the part missing will be rejected:
1. metadata - the metadata of the posts, including:
    - title
    - description
    - category
    - main_image: The source URL of banner image of the post
2. intro - the introduction of the post
    - intro_title
    - intro_content: The HTML content of the intro
3. rank_list - The items of rank list, should be exactly 10 items. Requests with more than or less than 10 rank items will be rejected. Each item includes:
    - sort_index: An integer for ordering
    - title
    - content: The HTML content of the rank item
### Example Request
```JavaScript
fetch("/PM/api/post/create/", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer xxxxxx.xxxxxxxx.xxxxxxxx"
    },
    body: JSON.stringify({
        "title": "Hello World",
        "description": "a hello world",
        "category":"meme",
        "main_image":"",
        "modify_user":1,
        "intro_title": "top 10 hello world",
        "intro_content":"<p>this rank shows top 10 hello worlds</p>",
        "rank_list": [
            {
                "sort_index": 1,
                "title": "hello world 1",
                "content": "<p>hello world 1 content</p>"
            },
            {
                "sort_index": 2,
                "title": "hello world 2",
                "content": "<p>hello world 2 content</p>"
            },
            {
                "sort_index": 3,
                "title": "hello world 3",
                "content": "<p>hello world 3 content</p>"
            },
            {
                "sort_index": 4,
                "title": "hello world 4",
                "content": "<p>hello world 4 content</p>"
            },
            {
                "sort_index": 5,
                "title": "hello world 5",
                "content": "<p>hello world 5 content</p>"
            },
            {
                "sort_index": 6,
                "title": "hello world 6",
                "content": "<p>hello world 6 content</p>"
            },
            {
                "sort_index": 7,
                "title": "hello world 7",
                "content": "<p>hello world 7 content</p>"
            },
            {
                "sort_index": 8,
                "title": "hello world 8",
                "content": "<p>hello world 8 content</p>"
            },
            {
                "sort_index": 9,
                "title": "hello world 9",
                "content": "<p>hello world 9 content</p>"
            },
            {
                "sort_index": 10,
                "title": "hello world 10",
                "content": "<p>hello world 10 content</p>"
            }
        ]
    })
})

```
### Example Response
```JSON
{
    "id": 1,
    "title": "Hello World",
    "description": "a hello world",
    "category": "meme",
    "main_image": "",
    "publish_date": "2024-03-30T17:58:45.875198",
    "last_modify": "2024-03-30T17:58:45.875262",
    "modify_user": 1,
    "intro_title": "top 10 hello world",
    "intro_content": "<p>this rank shows top 10 hello worlds</p>",
    "rank_list": [
        {
            "id": 1,
            "sort_index": 1,
            "title": "hello world 1",
            "content": "<p>hello world 1 content</p>"
        },
        {
            "id": 2,
            "sort_index": 2,
            "title": "hello world 2",
            "content": "<p>hello world 2 content</p>"
        },
        {
            "id": 3,
            "sort_index": 3,
            "title": "hello world 3",
            "content": "<p>hello world 3 content</p>"
        },
        {
            "id": 4,
            "sort_index": 4,
            "title": "hello world 4",
            "content": "<p>hello world 4 content</p>"
        },
        {
            "id": 5,
            "sort_index": 5,
            "title": "hello world 5",
            "content": "<p>hello world 5 content</p>"
        },
        {
            "id": 6,
            "sort_index": 6,
            "title": "hello world 6",
            "content": "<p>hello world 6 content</p>"
        },
        {
            "id": 7,
            "sort_index": 7,
            "title": "hello world 7",
            "content": "<p>hello world 7 content</p>"
        },
        {
            "id": 8,
            "sort_index": 8,
            "title": "hello world 8",
            "content": "<p>hello world 8 content</p>"
        },
        {
            "id": 9,
            "sort_index": 9,
            "title": "hello world 9",
            "content": "<p>hello world 9 content</p>"
        },
        {
            "id": 10,
            "sort_index": 10,
            "title": "hello world 10",
            "content": "<p>hello world 10 content</p>"
        }
    ]
}
```

## Retrieve a Post By ID
### URL
```
GET /PM/api/post/get/<post_id>/
```
### Authorization Type
Include the JWT Token in the request Header
```
Authorization: Bearer <JWT Token>
```
### Request Body
The request should not contain a body
### Example Request
```JavaScript
fetch("/PM/api/post/get/1/", {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer xxxxxx.xxxxxxxx.xxxxxxxx"
    }
})

```
### Example Response
```JSON
{
    "id": 1,
    "title": "Hello World",
    "description": "a hello world",
    "category": "meme",
    "main_image": "",
    "publish_date": "2024-03-30T17:58:45.875198",
    "last_modify": "2024-03-30T17:58:45.875262",
    "modify_user": 1,
    "intro_title": "top 10 hello world",
    "intro_content": "<p>this rank shows top 10 hello worlds</p>",
    "rank_list": [
        {
            "id": 1,
            "sort_index": 1,
            "title": "hello world 1",
            "content": "<p>hello world 1 content</p>"
        },
        {
            "id": 2,
            "sort_index": 2,
            "title": "hello world 2",
            "content": "<p>hello world 2 content</p>"
        },
        {
            "id": 3,
            "sort_index": 3,
            "title": "hello world 3",
            "content": "<p>hello world 3 content</p>"
        },
        {
            "id": 4,
            "sort_index": 4,
            "title": "hello world 4",
            "content": "<p>hello world 4 content</p>"
        },
        {
            "id": 5,
            "sort_index": 5,
            "title": "hello world 5",
            "content": "<p>hello world 5 content</p>"
        },
        {
            "id": 6,
            "sort_index": 6,
            "title": "hello world 6",
            "content": "<p>hello world 6 content</p>"
        },
        {
            "id": 7,
            "sort_index": 7,
            "title": "hello world 7",
            "content": "<p>hello world 7 content</p>"
        },
        {
            "id": 8,
            "sort_index": 8,
            "title": "hello world 8",
            "content": "<p>hello world 8 content</p>"
        },
        {
            "id": 9,
            "sort_index": 9,
            "title": "hello world 9",
            "content": "<p>hello world 9 content</p>"
        },
        {
            "id": 10,
            "sort_index": 10,
            "title": "hello world 10",
            "content": "<p>hello world 10 content</p>"
        }
    ]
}
```

## Update a Post by ID
### URL
```
PUT /PM/api/post/update/<post_id>/
```
### Authorization Type
Include the JWT Token in the request Header
```
Authorization: Bearer <JWT Token>
```
### Request Body
The post data, only the part that needs updating should be included, the format is similar to create a post with some exception:
1. the id of the post shouldn't be included
2. the id of the updating item in `rank_list` should be included
3. Creating new item is not allowed, requests with non-existing ids will be rejected
### Example Request
```JavaScript
fetch("/PM/api/post/update/1/", {
    method: "PUT",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer xxxxxx.xxxxxxxx.xxxxxxxx"
    },
    body: JSON.stringify({
        "title": "Goodby World",
        "rank_list": [
            {
                "id": 4,
                "content": "<p>This rank item has been changed</p>"
            }
        ]
    })
})

```
### Example Response
```JSON
{
    "id": 1,
    "title": "Goodby World",
    "description": "a hello world",
    "category": "meme",
    "main_image": "",
    "publish_date": "2024-03-30T17:58:45.875198",
    "last_modify": "2024-03-30T21:55:50.975475",
    "modify_user": 1,
    "intro_title": "top 10 hello world",
    "intro_content": "<p>this rank shows top 10 hello worlds</p>",
    "rank_list": [
        {
            "id": 1,
            "sort_index": 1,
            "title": "hello world 1",
            "content": "<p>hello world 1 content</p>"
        },
        {
            "id": 2,
            "sort_index": 2,
            "title": "hello world 2",
            "content": "<p>hello world 2 content</p>"
        },
        {
            "id": 3,
            "sort_index": 3,
            "title": "hello world 3",
            "content": "<p>hello world 3 content</p>"
        },
        {
            "id": 4,
            "sort_index": 4,
            "title": "hello world 4",
            "content": "<p>This rank item has been changed</p>"
        },
        {
            "id": 5,
            "sort_index": 5,
            "title": "hello world 5",
            "content": "<p>hello world 5 content</p>"
        },
        {
            "id": 6,
            "sort_index": 6,
            "title": "hello world 6",
            "content": "<p>hello world 6 content</p>"
        },
        {
            "id": 7,
            "sort_index": 7,
            "title": "hello world 7",
            "content": "<p>hello world 7 content</p>"
        },
        {
            "id": 8,
            "sort_index": 8,
            "title": "hello world 8",
            "content": "<p>hello world 8 content</p>"
        },
        {
            "id": 9,
            "sort_index": 9,
            "title": "hello world 9",
            "content": "<p>hello world 9 content</p>"
        },
        {
            "id": 10,
            "sort_index": 10,
            "title": "hello world 10",
            "content": "<p>hello world 10 content</p>"
        }
    ]
}
```

## Delete a Post by ID
### URL
```
DELETE /PM/api/post/delete/<post_id>/
```
### Authorization Type
Include the JWT Token in the request Header
```
Authorization: Bearer <JWT Token>
```
### Request Body
The request should not contain a body

### Example Request
```JavaScript
fetch("/PM/api/post/delete/3/", {
    method: "DELETE",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer xxxxxx.xxxxxxxx.xxxxxxxx"
    }
})

```
### Example Response
```JSON
{
    "detail": "Post deleted"
}
```