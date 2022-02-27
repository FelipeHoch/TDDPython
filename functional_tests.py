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
        header_text = self.browser.find_element('h1').text
        self.assertIn('To-Do', header_text)

        # Ela é convidada a inserir um item de tarefa imediatamente
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
            )

        # Ela digita "Comprar penas de pavão" em uma caixa de texto "o hooby de Bruna é fazer iscas para pescas com Felipe"
        input_box.send_keys('Comprar penas de pavão')

        # Quando ela tecla enter, a página é atualizada, e agora a página lista "1: Compre penas de pavão" como um item em uma
        # lista de tarefas
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_name('tr')
        self.assertTrue(
            any(row.text == '1: Compre penas de pavão')
            )

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')


# Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro item. Ela insere "Use penas de pavão"
# para fazer um fly - Bruna é bem metódica


# A página é atualizada novamente e agora mostra os dois itens em sua lista


# Bruna se pergunta se o site lembrará de sua lista. Então ela nota que o site gerou uma URL único para ela -- há um
# pequeno texto explicativo para isso.


# Ela acessa esse URL - sua lista de tarefas continua lá.

# Satisfeita, ela volta a dormir
