from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Jogo, Desenvolvedora, Plataforma


def lista_jogos(request):
    jogos = Jogo.objects.all().order_by('nome')

    pesquisa = request.GET.get('pesquisa', '')
    desenvolvedora = request.GET.get('desenvolvedora', '')
    plataforma = request.GET.get('plataforma', '')

    if pesquisa:
        jogos = jogos.filter(nome__icontains=pesquisa)

    if desenvolvedora:
        jogos = jogos.filter(desenvolvedora_id=desenvolvedora)

    if plataforma:
        jogos = jogos.filter(plataforma_id=plataforma)

    desenvolvedoras = Desenvolvedora.objects.all()
    plataformas = Plataforma.objects.all()

    paginator = Paginator(jogos, 5)
    pagina = request.GET.get('page')
    jogos = paginator.get_page(pagina)

    return render(request, 'catalogo/lista.html', {
        'jogos': jogos,
        'desenvolvedoras': desenvolvedoras,
        'plataformas': plataformas,
        'pesquisa': pesquisa,
        'desenvolvedora_selecionada': desenvolvedora,
        'plataforma_selecionada': plataforma,
    })