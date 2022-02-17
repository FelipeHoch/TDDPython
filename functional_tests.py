import unittest

from selenium import webdriver


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
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')


# Ela é convidada a inserir um item de tarefa imediatamente


# Ela digita "Comprar penas de pavão" em uma caixa de texto "o hooby de Bruna é fazer iscas para pescas com Felipe"


# Quando ela tecla enter, a página é atualizada, e agora a página lista "1: Compre penas de pavão" como um item em uma
# lista de tarefas


# Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro item. Ela insere "Use penas de pavão"
# para fazer um fly - Bruna é bem metódica


# A página é atualizada novamente e agora mostra os dois itens em sua lista


# Bruna se pergunta se o site lembrará de sua lista. Então ela nota que o site gerou uma URL único para ela -- há um
# pequeno texto explicativo para isso.


# Ela acessa esse URL - sua lista de tarefas continua lá.

# Satisfeita, ela volta a dormir
