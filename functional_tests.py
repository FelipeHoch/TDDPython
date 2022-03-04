import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Bruna ouviu falar de uma nova aplicação online interessante lista de tarefas. Ela decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        # Ela percebe quue o título da página e o cabeçalho mencionam listas de tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ela é convidada a inserir um item de tarefa imediatamente
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Ela digita "Comprar penas de pavão" em uma caixa de texto "o hooby de Bruna é fazer iscas para pescas com Felipe"
        inputbox.send_keys('Comprar penas de pavão')

        # Quando ela tecla enter, a página é atualizada, e agora a página lista "1: Compre penas de pavão" como um item em uma
        # lista de tarefas
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Comprar penas de pavão', [row.text for row in rows])  

        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro item. Ela insere "Use penas de pavão"
        # para fazer um fly - Bruna é bem metódica
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Usar penas de pavão para fazer um fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)


        # A página é atualizada novamente e agora mostra os dois itens em sua lista
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertIn('1: Comprar penas de pavão', [row.text for row in rows])
        self.assertIn('2: Usar penas de pavão para fazer um fly',
            [row.text for row in rows])


        # Bruna se pergunta se o site lembrará de sua lista. Então ela nota que o site gerou uma URL único para ela -- há um
        # pequeno texto explicativo para isso.
        self.fail('Finish the test!')


        # Ela acessa esse URL - sua lista de tarefas continua lá.


if __name__ == '__main__':
    unittest.main(warnings='ignore')


# Satisfeita, ela volta a dormir
