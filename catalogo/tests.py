from django.test import TestCase
from django.urls import reverse
from .models import Jogo, Desenvolvedora, Plataforma


class CatalogoTests(TestCase):

    def setUp(self):
        self.dev = Desenvolvedora.objects.create(
            nome='Rockstar Games'
        )

        self.plat = Plataforma.objects.create(
            nome='PC'
        )

        for i in range(1, 7):
            Jogo.objects.create(
                nome=f'GTA {i}',
                desenvolvedora=self.dev,
                plataforma=self.plat
            )

    def test_listagem(self):
        resposta = self.client.get(reverse('lista_jogos'))
        self.assertEqual(resposta.status_code, 200)

    def test_pesquisa(self):
        resposta = self.client.get(
            reverse('lista_jogos'),
            {'pesquisa': 'gta 1'}
        )

        self.assertEqual(
            resposta.context['jogos'].paginator.count, 1
        )

    def test_filtros(self):
        resposta = self.client.get(
            reverse('lista_jogos'),
            {
                'desenvolvedora': self.dev.id,
                'plataforma': self.plat.id
            }
        )

        self.assertEqual(
            resposta.context['jogos'].paginator.count, 6
        )

    def test_paginacao(self):
        resposta = self.client.get(reverse('lista_jogos'))

        self.assertEqual(len(resposta.context['jogos']), 5)

    def test_preservacao_dos_filtros(self):
        resposta = self.client.get(
            reverse('lista_jogos'),
            {
                'pesquisa': 'GTA',
                'desenvolvedora': self.dev.id,
                'plataforma': self.plat.id,
                'page': 2
            }
        )

        self.assertEqual(resposta.context['pesquisa'], 'GTA')
        self.assertEqual(resposta.context['jogos'].number, 2)
        self.assertEqual(len(resposta.context['jogos']), 1)