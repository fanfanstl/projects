# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get('https://flight.qunar.com/')
#
# driver.implicitly_wait(10)
#
#
# end_input = driver.find_element_by_xpath('//input[@name="toCity"]')
# end_input.send_keys("成都")
# time.sleep(0.1)
# end_input.click()
# time.sleep(0.2)
# end_input.send_keys(Keys.RETURN)
#
# search_button = driver.find_element_by_xpath('//*[@id="dfsForm"]/div[4]/button')
# search_button.click()
# driver.implicitly_wait(10)
# data_divs = driver.find_elements_by_xpath('//div[@class="m-airfly-lst"]//div[@class="b-airfly"]')
# for div in data_divs:
#     title = div.find_elements_by_xpath('.//div[@class="air"]//span')[0].text
#     start_time = div.find_elements_by_xpath('.//div[@class="col-time"]//h2')[0].text
#     end_time = div.find_elements_by_xpath('.//div[@class="col-time"]//h2')[1].text
#     price = div.find_elements_by_xpath('.//p[@class="prc"]//em//b//i')
#     price_list = [i.text.strip() for i in price]
#     price_swp = div.find_elements_by_xpath('//p[@class="prc"]//em//b[position()>1]')
#     for swp in price_swp:
#         # print(int(swp.value_of_css_property("left")[:-2]),swp.value_of_css_property("width")[:-2])
#         index = int(int(swp.value_of_css_property("left")[:-2])/int(swp.value_of_css_property("width")[:-2]))
#         print(index,swp.text)
#         price_list[index] = swp.text.strip()
#     price = ''.join(price_list)
#     print(title,start_time,end_time,price)
#
#
#
# # for em in em_lists:
# #     i_lists = em.find_elements_by_xpath('.//b[1]//i')
# #     data = [i.text for i in i_lists]
# #     print(data)
# #     # meta_data.append(data)
# #     b_lists = em.find_elements_by_xpath('.//b')[1:]
# #     for b in b_lists:
# #         width = int(b.value_of_css_property("width")[:-2])
# #         left = int(b.value_of_css_property("left")[:-2])
# #         swp_index = int(left/width)
# #         print(swp_index)
# #         data[swp_index] = b.text.strip()
# #         data = ''.join(data)
# #     meta_data.append(data)
# # print(meta_data)
#
#
#
#
#
#
#
#
#
#
#
#
