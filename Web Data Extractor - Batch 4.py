#Install required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime as dt
from tqdm import tqdm

#pip freeze > requiremnts.txt


main_url = "https://unique.com.mm/collections/mobile-phone"

"""Create the main URLs """


def create_url(web_url):
    #Step 1 - Request data from the website
    #Get data by using URL
    response = requests.get(web_url)

    #Extract html,css,etc. 
    web_data = response.text

    #Step 2 - Create beautifulsoup object to read web data
    bsObj = BeautifulSoup(web_data,"html5lib")


    #Step 3 - Extract Last page number
    last_page_tag_list = bsObj.find_all("a", "pagination__nav-item link")
    last_page_tag= last_page_tag_list[-1]    #This is the last one of the list.
    last_page_text = last_page_tag.text
    last_page_text= int(last_page_text)

    #Step 4 - Create URL for other web pages
    #print(list(range(2,last_page_text+1)))             #The last page can vary so we put + 1 here. The range will show one less the actual number so we have to add 1 to the last page.
    created_url_list = []
    created_url_list.append(web_url)
    for number in range (2,last_page_text+1):
        new_url = web_url+ "?page=" + str(number)
        #print(new_url)
        created_url_list.append(new_url)
        
    print("URL links are created successfully.")
    return created_url_list               #We have to make a return here or else only none will come out.
    

"""Create current date time string"""
def get_current_dt():
    #Get current date and time
    current_datetime = dt.now()     # or current_dt = datetime.now()   #datetime class and datetime module has beem imported.
    #Change date tp string
    current_datetime= str(current_datetime)
    #replace : with -
    current_datetime = current_datetime.replace(":", "-")
    #remove millisecond
    current_datetime= current_datetime.split(".")[0]
    return current_datetime

"""Extract product info tag and return as a list """
def get_product_info_tags(url):
    #Get data by using URL
    response = requests.get(url)

    #Extract html,css,etc. 
    web_data = response.text

    #print(web_data)

    #Step 2 - Create beautifulsoup object to read web data
    bsObj = BeautifulSoup(web_data,"html5lib")

    #Step 3 - Extract and insert data into the list
    #Extract all product info main tags
    product_info_tags_list = bsObj.find_all("div", "product-item__info-inner")
    return product_info_tags_list

def create_name_list(product_info_tags_list):
    """Extract product name from the product info tag and create a product name list"""
    name_list = []
    for product_info_tag in product_info_tags_list:
        #Extract product name tag
        product_name_tag = product_info_tag.find("a","product-item__title text--strong link")
        #Extract product name
        product_name = product_name_tag.text
        name_list.append(product_name)
    return name_list





def create_price_list(product_info_tags_list):
    """Extract product price from the product info tag and create a product price list"""
    price_list= []
    for product_info_tag in product_info_tags_list: 
        #Extract product price tag
        product_price_tag = product_info_tag.find("div","product-item__price-list price-list")
        #Extract product price
        product_price = product_price_tag.text        #.text is attribute
        #Transform product price

        product_price=product_price.replace(",","")  #Remove , from the product price
        product_price = product_price.replace("K","") #Remove K from the product price text
        try:
            
            product_price = int(product_price)   #Change data type
            price_list.append(product_price)
        except ValueError:
            #Handle the discount price
            product_price = '769900\n              799900'

            discont_price_list = product_price.split("\n")

            #Get the last value
            product_price= discont_price_list[-1]
            
            #Remove the spaces from the text
            product_price = product_price.strip()
            price_list.append(product_price)
            
    return price_list


""""""
def create_status_list(product_info_tags_list):
    """Extract product status from the product info tag and create a product status list"""
    
    status_list = []

    for product_info_tag in product_info_tags_list:

        # Extract product status tag
        # Error handling for high inventory status vs no inventory

        status_class_list = [
            "product-item__inventory inventory",
            "product-item__inventory inventory inventory--high",
            "product-item__inventory inventory inventory--low"
        ]

        for status_class in status_class_list:
            result = product_info_tag.find("span", status_class)

            if result != None:
                product_status_tag = result
                product_status = product_status_tag.text.strip()
                status_list.append(product_status)

            

    return status_list
########################### Main Program ###############################

def main():
    """Main Programe to extract data from the website"""
    
    #Step 1 - Create URL for all pages 
    url_list = create_url(main_url)


    #Step 2 - Extract Data from Each URL of the URL List.
    count = 0
    url_count = 0
    final_df = pd.DataFrame()  #Create an empty dataframe 
    for each_url in tqdm(url_list):
        #Extract product info tags:
        p_info_tags_list = get_product_info_tags(each_url)
        
        #Create Product name list
        p_name_list = create_name_list(p_info_tags_list)
        
        #Create product price list
        p_price_list = create_price_list(p_info_tags_list)
        
        #Create product status list
        p_status_list = create_status_list(p_info_tags_list)
        #print(p_name_list)
        #print(p_price_list)
        #print(p_status_list)
        
        #Create page level data frame
        
        page_df = pd.DataFrame({"Product Name":p_name_list,
                           "Price":p_price_list,
                            "Status":p_status_list})
        
        ##Get current date time as string
        current_dt = get_current_dt()
        url_count+=1
        #Export as page level excel file 
        #Step 5 - Export as an Excel file
        #df.to_excel(f"Output2{url_count}.xlsx", index = False)\
        page_df.to_excel(f"Output_{url_count}_{current_dt}.xlsx", index=False) 
        
        #print(f"Web page {url_count} is completed sucessfully!")
        
        # Export data from all pages
        final_df = pd.concat([final_df, page_df])         #Concact is merging the data frames - pd.concat ([])
                                                  

    #Export the final data frame as an excel file
    final_df.to_excel("All Data_{current_dt}.xlsx",index = False)

    print("Project is completed successfully")
       
if __name__== "__main__":  
    main()

