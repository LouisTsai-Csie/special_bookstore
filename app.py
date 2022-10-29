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
        if target not in name: continue
        name.strip()
        district = name[5:]
        if len(district) == 0: continue
        if district not in optionList:
            optionList.append(district)
    return optionList

def getSpecificBookstore(items, county, districts):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        # 如果 name 不是我們選取的 county 則跳過
		# hint: 用 if-else 判斷並用 continue 跳過
        
		# districts 是一個 list 結構，判斷 list 每個值是否出現在 name 之中
		# 判斷該項目是否已經出現在 specificBookstoreList 之中，沒有則放入
		# hint: 用 for-loop 進行迭代，用 if-else 判斷，用 append 放入
    return specificBookstoreList

def app():
	bookstoreList = getAllBookstore()

	countyOption = getCountyOption(bookstoreList)
    
    st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', countyOption) 
	districtOption = getDistrictOption(bookstoreList, county)
	district = st.multiselect('請選擇區域', districtOption) 
	
	# 呼叫 getSpecificBookstore 並將回傳值賦值給變數 specificBookstore
	num = len(specificBookstore)
	# 用 st.write 將目標書店的總數量計算出來，格式：總共有3項結果
	

if __name__ == '__main__':
    app()