
import os
import time
import glob2
from selenium import webdriver
# Import selenium module of python


def transfer(path):
    """
    This function is used to access Google translate, first get the path of the file, and then send it to the browser.
    :param path: The absolute path of the file you want to translate.
    :return: empty
    """
    print("path",path)
    browser = webdriver.Chrome()
    # Create browser objects

    browser.get('https://translate.google.cn/'
                '?hl=en&tab=TT&sl=en&tl=hi&op=translate')
    # Visit Google Translate's website
    # The parameters inside set the language translation, which we can modify. Here is to translate Chinese into English

    h1 = browser.current_window_handle
    # Record current page
    # This operation is to place it. After clicking, we can't find the page we want

    ele = browser.find_elements_by_tag_name("button")
    # Get the button tag and click button
    # Here, the method of obtaining the button through the tag name is used to obtain the tag, which is convenient for subsequent click operations

    ele[1].click()
    # Click button

    all_h = browser.window_handles
    # Get all pages

    browser.switch_to.window(all_h[0])
    # Select the current page
    h2 = browser.current_window_handle

    upload = browser.find_element_by_id('i34')
    # Get the label of the button that gets "add file"
    # The id of this tag is obtained by checking the web page

    upload.send_keys(path)
    # Upload file
    # Path is the absolute path of the file, which we choose to specify

    print(upload.get_attribute('value'))
    # Print the path to the display file

    browser.find_elements_by_tag_name("button")[39].click()
    # This is the translation button after successfully uploading the file

    
    res = browser.page_source
    # This is to get the content of the page


    with open("result.txt", "a+") as f:
        # Here is to write the translation results to a file
        # Open a file and write the contents to it

        print(res[30: len(res) - 20])
        # Displays the results of the translation
        
        f.write(res[30: len(res) - 20])
        # Write the translation results to the file
        
        f.close()
        # You still need to close the file after the operation is completed     

    browser.close()
    # After all operations are completed, you need to close the browser
    time.sleep(6)


if __name__ == '__main__':
    # main function
    # This is a test
    c=0
    path = '/home/rati/Downloads/google_translation/extracted/'
    for filename in glob2.glob(os.path.join(path, '*.txt')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
        # do your stuff
            c+=1

    # Pass the location of the file to the formal parameter path
    print(c)
    for i in range(1,c+1):
        
        name = str(i)
        # filename = "%s.txt" % name
        p=path+"%s.txt" % name
        transfer(path=p)
