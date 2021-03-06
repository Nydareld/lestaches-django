from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

class NewTaskTest(TestCase):

    '''Test d'ajout et supression d'une tache '''
    def test_add_task(self):

        browser = webdriver.Chrome()
        browser.get('http://localhost:8000/newTask')
        time.sleep(1)

        name = browser.find_element_by_id("id_name")
        desc = browser.find_element_by_id("id_description")

        name.send_keys("Ma super tache")
        time.sleep(1)

        desc.send_keys("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        time.sleep(1)

        browser.find_element_by_id("submit").click()
        time.sleep(1)

        #Là la tache doit etre crée
        noms = browser.find_elements_by_css_selector("body > div > div > section.content-header > div > div > div > div.box-header > a > h4")
        time.sleep(1)
        taskFound = False
        elem = None
        for nom in noms:
            if( re.match("Ma super tache", nom.text) ):
                taskFound = True
                elem = nom

        #la tache est crée
        self.assertEqual(True,taskFound)

        #mnt on click pour l'afficher
        elem.click()
        time.sleep(1)
        #mnt on va la supprimer
        browser.find_elements_by_css_selector("body > div > div > section.content-header > h1 > span > a:nth-child(1) > i")[0].click()
        time.sleep(1)

        #on verrifie qu'elle est supprimée
        noms = browser.find_elements_by_css_selector("body > div > div > section.content-header > div > div > div > div.box-header > a > h4")
        taskFound = False
        for nom in noms:
            if( re.match("Ma super tache", nom.text) ):
                taskFound = True

        #la tache est crée
        self.assertEqual(False,taskFound)
        time.sleep(1)
        

        browser.quit()
