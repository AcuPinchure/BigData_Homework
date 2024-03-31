from django.core.management.base import BaseCommand

from django.contrib.auth.models import User
from post_management.models import Post, RankItem


class Command(BaseCommand):
    help = "Create default user if there is no user in the database."

    def handle(self, **options):
        if not User.objects.exists():
            user = User.objects.create_superuser(
                username="djangoadmin",
                email="user@example.com"
            )
            user.set_password("djangoadmin")
            user.save()

            self.stdout.write(self.style.SUCCESS("Successfully created a superuser"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser already exists"))

        if not Post.objects.exists():
            post_1 = Post.objects.create(
                title="「如果我能向神龍許願…」鳥山明經典神作《七龍珠》10大人氣角色誰是冠軍？　原來阿拉蕾也曾幫助悟空",
                description="《七龍珠》作者鳥山明逝世，《DailyView網路溫度計》和你一起回顧那些童年中的經典角色。",
                category="動漫",
                main_image="https://dailyview.tw/_next/image?url=https%3A%2F%2Fdvblobcdnjp.azureedge.net%2FContent%2FUpload%2FDailyArticle%2FImages%2F2024-03%2F2a64a093-c63b-458b-a5b5-fc7824b60939_m.jpg&w=1920&q=75",
                modify_user=user,
                intro_title="永遠的經典神作《七龍珠》",
                intro_content=r"""<div aria-hidden="true" class="Templates_theme_content__x7n8g"><p style="text-align: justify;">日本經典少年漫畫《七龍珠》（ドラゴンボール／DRAGON BALL）的作者鳥山明於8日傳出逝世消息，《七龍珠》系列官方網站發出公告，表示鳥山明已於1日因急性顱內出血病逝，享壽68歲，許多動漫迷們都感到不捨與惋惜。<a href="https://dailyview.tw/" target="_blank">《DailyView網路溫度計》</a>透過<a href="https://keypo.tw/" target="_blank">《KEYPO大數據關鍵引擎》</a>輿情分析系統，調查出其代表作《七龍珠》系列的10大人氣角色，回憶經典的同時，也感謝老師所留下的美好故事。</p><p style="text-align: justify;">悟空、悟飯、弗利沙、特南克斯、普烏……這些角色們，是否也佔據了你的童年呢？即便在長大後，《七龍珠》也依然帶給許多人力量，改編、續作、電影版及相關周邊更是熱銷不斷，成為現象級的作品。在這部經典中，你最喜歡哪個角色呢？快來看看他有沒有上榜吧！</p><p style="text-align: justify;"><span style="font-size: 12px;">image source: X／<a href="https://twitter.com/DB_official_jp/status/1751151179051254009/photo/1" target="_blank">ドラゴンボールオフィシャル</a></span></p></div>"""
            )
            rank_list = [
                RankItem(sort_index=1, title="NO. 10 比克", post=post_1, content=r"""<div aria-hidden="true"><p style="text-align: justify;">比克為比克大魔王的兒子，為了向悟空報殺父之仇而以「魔少年」的身分參加第23回天下第一武道會，以打倒同樣參戰的悟空為目標。不過原先抱持著復仇心態的比克，卻在和悟空一行人接觸的過程中受到影響，也漸漸改邪歸正，成為悟空的同伴之一。<br></p><p style="text-align: justify;">後期比克和天神合體，實力大增，並擁有必殺技「魔貫光殺炮」，為了讓比克能使用絕招殺掉拉帝茲，悟空選擇犧牲自己，而比克也親自訓練悟空的兒子悟飯，兩人的師徒情誼是不少人最喜歡的地方，網友們紛紛表示：「比克真的是好父親」、「史上最佳保母」。</p></div>"""),
                RankItem(sort_index=2, title="NO. 9 黑悟空", post=post_1, content=r"""<div aria-hidden="true"><p style="text-align: justify;">黑悟空為《七龍珠超》在未來世界出現的敵人，外貌和悟空非常相似，其真實身分為後現代世界的界王神扎馬斯。在另一個時空中，實習界王神扎馬斯成功弒師，搶奪「波特拉耳環」及「時空戒指」，並使用超級七龍珠和悟空交換身體，成為黑悟空。<br></p><p style="text-align: justify;">為了執行「人類歸零計畫」（人間0計画），黑悟空消滅了許多星球的人，同時殺掉全宇宙的界王神。黑悟空性格高傲自負，思想絕對，總是以凌駕於萬物之上的姿態審視著人類，蔑視一切的態度讓許多人印象深刻，也有不少網友認為黑悟空是《七龍珠》系列裡「最帥的角色」。</p></div>"""),
                RankItem(sort_index=3, title="NO. 8 特南克斯", post=post_1, content=r"""<div aria-hidden="true"><p style="text-align: justify;">特南克斯為賽亞人王子貝吉塔和地球科學家布瑪的兒子，是保衛地球的Z戰士之一。在《七龍珠》系列中，為了拯救未來，特南克斯乘坐母親發明的時光機回到過去，總空出現在4個不同的時空中，阻止人造人穿越時空回到過去，也將未來的心臟病特效藥透過母親轉交給悟空。<br></p><p style="text-align: justify;">在賽魯遊戲結束後，克南特斯回到原本的時空，除了解決掉人造人之外，也揭穿了的賽魯想利用時光機回到過去的企圖，同時殺掉賽魯，讓世界恢復和平。帥氣的特南克斯也是許多人最喜歡的角色，「小時候覺得特南克斯超帥，電玩都要選他」。</p></div>"""),
                RankItem(sort_index=4, title="NO. 7 布羅利", post=post_1, content=r"""<div aria-hidden="true"><p style="text-align: justify;">布羅利為喜歡殺戮的「傳說中的超級賽亞人」倖存者，是《七龍珠》動畫劇場版中的原創角色。只懂得破壞的布羅利力量遠高於貝吉塔星的其他賽亞人，一出生就擁有一萬戰鬥力，也因為戰鬥太高而和父親一同被貝吉塔王流放。<br></p><p style="text-align: justify;">天生性格殘暴、好戰的布羅利，壓倒性的實力就連悟空、悟飯、貝吉塔、特南克斯、比克等人聯手都無法對付。在劇場版登場後，布羅利獲得超高人氣，原作者鳥山明更親自重製該劇場版，布羅利絕對的戰力震撼許多網友，「小時候看到布羅利真的怕爆」、「絕望程度歷代最強」。</p></div>"""),
                RankItem(sort_index=5, title="NO. 6 弗利沙", post=post_1, content=r"""<div aria-hidden="true"><p style="text-align: justify;">弗利沙為《七龍珠》中最主要的反派角色，擁有「宇宙帝王」的稱號，帶著與生俱來的強大戰鬥力和進化變身能力，性格兇殘狡詐的他毀滅了賽亞人的貝吉塔行星，並且試圖透過七龍珠實現長生不老。<br></p><p style="text-align: justify;">在故事中，弗利沙有多種形態，他來到地球之後便被特南克斯殺死，並且和自己的手下一起下了地獄。在《七龍珠超》的宇宙生存篇中，弗利沙和悟空合作擊敗吉連，也因此立下功勞，被破壞神比魯斯賦予復活的獎勵。這段劇情也讓許多網友印象深刻：「在最後跟悟空一起打吉連，雙雄連手出擊定勝負，根本就是名場面。」</p></div>"""),
                RankItem(sort_index=6, title="NO. 5 孫悟飯", post=post_1, content=r"""<div aria-hidden="true"><p style="text-align: justify;">悟飯為悟空和琪琪的長子，被悟空以養父的名字來命名。悟飯雖然自出生就擁有強大的力量和潛力，但並不像父親悟空一樣好戰，在母親的指點之下勤奮學習，夢想是成為一名學者。雖然性格善良不喜歡戰鬥，不過在憤怒時也能發揮強大的力量。<br></p><p style="text-align: justify;">在悟空前往陰間修練時，悟飯拜比克為師，在其指導之下學習武功，兩人之間深厚的情誼是不少粉絲在《七龍珠》系列作品中最喜歡的部分。悟飯曾參與與弗利沙的戰鬥，之後也曾數次變成超級賽亞人2，許多網友高度認可他的實力，「悟飯一直（潛力）最強」。</p></div>"""),
                RankItem(sort_index=7, title="NO. 4 神龍", post=post_1, content=r"""<div aria-hidden="true"><p style="text-align: justify;">在《七龍珠》中，神龍為收集到7顆龍珠後方可召喚的神明。只要集齊7顆龍珠後唸出咒語，就可以召喚出神龍並且向其許願，在願望實現後，7顆龍珠會自動飛散，化作石頭，一年後才可以再度使用。原先一次最多只能實現1個願望，在天天成為新神後，轉為一次可以實現3個願望。<br></p><p style="text-align: justify;">集齊七龍珠向龍神許願，這大概是所有喜歡《七龍珠》的人都曾經有過的夢想。在鳥山明老師傳出逝世消息後，《火影忍者》作者岸本齊史在弔唁文感嘆：「如果我能向神龍許一個願望就好了……對不起……這或許是很任性的要求吧。」</p></div>"""),
                RankItem(sort_index=8, title="NO. 3 貝吉塔", post=post_1, content=r"""<div aria-hidden="true"><p style="text-align: justify;">貝吉塔為貝吉塔行星的賽亞人王子，曾經效力於弗利沙，為了搶奪七龍珠實現永生的願望，貝吉塔和那霸一同來到地球，在初次登場是一名侵略者。不過被悟空等人聯手擊敗後，貝吉塔就以超越悟空為目標留在地球，受到悟空等人的影響，漸漸改邪歸正，成為重要角色之一。<br></p><p style="text-align: justify;">起初只是為了超越悟空留下，不過後來貝吉塔在此有了家人，也漸漸愛上這個地方，之更多次和悟空一同保護地球。在與魔人普烏一戰中，為了保護地球貝吉普甚至決定與其同歸於盡，前後的轉變吸引到許多粉絲，網友紛紛表示「男子漢的帥」、「直接昇華成最受歡迎的角色」。</p></div>"""),
                RankItem(sort_index=9, title="NO. 2 魔人普烏", post=post_1, content=r"""<div aria-hidden="true"><p style="text-align: justify;">魔人普烏是由邪惡魔導士比比提喚醒的反派角色，擁有無限的再生能力，只有還有一個細胞未被消滅都可以再生，也可以將別人吸收，成為自己身體的一部分。最初的普烏性格兇殘，被撒旦先生感化後體內的邪惡部分被逼出，化身為邪惡（瘦普烏）及善良（胖普烏）兩個普烏。<br></p><p style="text-align: justify;">不過邪惡普烏先後吸收了善良普烏、悟飯、悟天克斯、比克等人，之後甚至還將地球毀滅，最後悟空透過神龍許願，復活地球上的人並收集能量製造元氣彈，才成功將其消滅。除了能力外，普烏的外型其實也備受網友討論，「小時候比較喜歡瘦普烏」、「一直都是喜歡胖普烏」、「胖普烏可愛」。</p></div>"""),
                RankItem(sort_index=10, title="NO. 1 孫悟空", post=post_1, content=r"""<div aria-hidden="true"><p style="text-align: justify;">孫悟空為來自貝吉達行星、原名「卡卡洛特」的賽亞人，這個名字源自於日文的「胡蘿蔔」（キャロット, Carrot），以下級戰士的身分被送往地球，並被武道家孫悟飯收養，在悟飯逝世後便獨自生活。某日結識布瑪後，因而踏上了尋找龍珠的旅程，在過程中為了變得更強不斷刻苦修行。<br></p><p style="text-align: justify;">性格坦率又認真的悟空，是許多人最喜歡的角色，在戰鬥中即使面對惡人，也不會輕取他人性命。鳥山明曾表示，悟空戰鬥最大的理由，其實都出自於想要「變得更強」，這樣的特質以及在過程中的不斷成長，也深深吸引著讀者：「他很有擔當、很勇敢」、「一路以來越來越厲害，還很正義」。</p></div>"""),
            ]
            RankItem.objects.bulk_create(rank_list)


        
