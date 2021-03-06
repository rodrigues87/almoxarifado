from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
import jwt
import json
from collections import namedtuple
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.core import serializers

from almoxarifado.settings import GROUP_REDIRECT_URL
from cadastro.models import Cadastro
from locais.models import Locais
from permissao.models import Permissao


def HomepageView(request):
    redirect_to = settings.LOGIN_REDIRECT_URL

    response = request.COOKIES.get('JWT-TOKEN-CB')

    print(response)

    if str(response) == 'None':
        return HttpResponseRedirect("http://portal.cb.es.gov.br/portal-cbmes/")

    else:
        decodedPayload = jwt.decode(response, None, None)

        print(decodedPayload)

        jsonValue = json.dumps(decodedPayload)

        # serialized_obj = serializers.serialize('json', [obj, ])

        jonObject = json.loads(jsonValue, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        print(jonObject.sub, jonObject.usuario.nome, jonObject.usuario.postoGraduacao)

        user = authenticate(username=jonObject.sub, password='Bombeiros2019')
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(redirect_to)
        else:

            user = User.objects.create_user(
                username=jonObject.sub,
                password='Bombeiros2019',
                email=jonObject.usuario.email,
            )

            user.is_staff = True

            user.save()

            cadastro = Cadastro.objects.create(
                user=user,
                postoGraduacao=jonObject.usuario.postoGraduacao,
                nome=jonObject.usuario.nome,
                oficial=jonObject.usuario.oficial,
                nomeGuerra=jonObject.usuario.nomeGuerra,
                numeroFuncional=jonObject.usuario.numeroFuncional,
                localQo=jonObject.usuario.locais.localQo.nome,
                localQdi=jonObject.usuario.locais.localQdi.nome,
                cpf=jonObject.usuario.cpf,
            )

            for permissao in jonObject.roles:
                try:
                    perm = Permissao.objects.get(nome=permissao)

                except Permissao.DoesNotExist:
                    perm = Permissao.objects.create(nome=permissao)

                cadastro.permissao.add(perm)

            for permissaoIntranet in jonObject.rolesIntranet:
                try:
                    permIntranet = Permissao.objects.get(nome=permissaoIntranet)

                except Permissao.DoesNotExist:
                    permIntranet = Permissao.objects.create(nome=permissaoIntranet)

                cadastro.permissao.add(permIntranet)

                my_group = Group.objects.get(name='almoxarife')
                my_group.user_set.add(user)

            """
            localAdido = jonObject.usuario.locais.localAdido

            localQdi = Locais.objects.create(
                sigla="x.usuario.locais.localQdi.sigla",
                nome="teste",
            )
            localQdi.save()

            localQo = Locais.objects.create(
                sigla="x.usuario.locais.localQo.sigla",
                nome="teste",
            )
            localQo.save()

            locais = Locais.objects.create(
                localQo=localQo,
                localQdi=localQdi,
                localAdido=localAdido,
            )

            locais.save()
"""

            # cadastro.local.localQdi =x.usuario.locais.localQdi
            # cadastro.local.localQo = x.usuario.locais.localQo

            login(request, user)
            return HttpResponseRedirect(redirect_to)

    """
    @method_decorator(ensure_csrf_cookie)
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)
        """


# ------------------------------------------------------------------
""" main.js (with some code adapted from Django official site)
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== ‘’) {
        var cookies = document.cookie.split(‘;’);
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Check if this cookie string begin with the name we want
            if (cookie.substring(0, name.length + 1) === (name + ‘=’)) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
             }
         }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader(“X-CSRFToken”, getCookie(‘csrftoken’));
        }
    }
});
// actual AJAX call
$.ajax({
    method: “POST”,
    url: “/postcodes”,
    contentType: ‘application/json’,
    data: JSON.stringify(input),
    dataType: “json”,
    success: function(data) {
        // do something
    }
 })
    """
