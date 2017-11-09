# 利用scrapy 取得台灣彩卷的號碼並將資料存在csv中
> lotte.csv -->產生出來樂透的資料 <br>
> items.py --> scrapy 的item物件（資料）<br>
> pipelines.py --> scrapy的資料儲存和處理的地方<br>
> setting.py --> scrapy的設定值，其中要使用pipelines也必須從這設定中打開 <br>
>> ITEM_PIPELINES = {  <br>
>>    'lotter.pipelines.LotterPipeline': 300, <br>
>> }  <br>
> AppleCrawler.py --> 資料取得的地方其中name即是要呼叫時使用，在此的name = 'lotter' <br>
>> scrapy crawl apple  <br>
