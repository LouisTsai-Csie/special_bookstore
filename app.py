import streamlit as st
import requests

def getAllBookstore() ->list:
    url = "https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def getCountyOption(items) ->list:
    optionList = []
    for item in items:
        name = item['cityName'][0:3]
        if name not in optionList:
            optionList.append(name)
    return optionList

def getDistrictOption(items, target) ->list:
    optionList = []
    for item in items:
        name = item['cityName']
        # 如果 name 裡面不包含我們選取的縣市名稱(target) 則略過該次迭代
		# hint: 使用 if-else 判斷式並且用 continue 跳過
				
        name.strip()
        district = name[5:]
        if len(district) == 0: continue

        # 如果 district 不在 optionList 裡面，將 district 放入 optionList
		# hint: 使用 if-else 判斷式並使用 append 將內容放入 optionList

    return optionList

def app():
	bookstoreList = getAllBookstore()

	countyOption = getCountyOption(bookstoreList)

    st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', countyOption) 
	# 呼叫 getDistrictOption 並將回傳值賦值給變數 districtOption
	district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd']) # 將['a', 'b', 'c', 'd']替換成縣市選項

if __name__ == '__main__':
    app()