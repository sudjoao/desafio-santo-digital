# Intership Challenge SantoDigital

## Sobre
Desenvolvimento de uma API que retorne campos específicos de uma NF a partir do JSON fornecido pelo Google Vision API.

As imagens utilizadas para a API foram DANFE (Documento Auxiliar da NF-e), existem algumas disponíveis para teste na pasta images

## Rodar localmente
### Instalações

#### 1. [Docker](https://www.docker.com/products/docker-desktop)

### Execução
##### 1. Entrar na pasta raiz
```
cd Desafio/
```
#### 2. Buildar o docker
```
docker build --tag project  .
```
#### 3. Rodar o servidor
```
docker run --publish 5000:5000 project
```

<br>
<br>

#  Rotas
## GET /
#### Parameters
-
### Reponse
| Name | Type | Description |
|:----:|:----:|:-----------:|
| message | ```string```  | Mensagem Hello World para saber que o server está up|

## POST /invoice

#### Parameters
* JSON fornecido pelo Google Cloud Vision


#### Exemplo
```json
{
    "cropHintsAnnotation": "...",
    "fullTextAnnotation": "...",
    "imagePropertiesAnnotation": "...",
    "labelAnnotations": "...",
    "localizedObjectAnnotations": "...",
    "safeSearchAnnotation": "...",
    "textAnnotations": "...",
}
```

### Reponse
| Name | Type | Description |
|:----:|:----:|:-----------:|
| invoice_number | ```string```  | Número da Nota Fiscal |
| value | ```string```  | Valor total da nota fiscal |
| verification_code | ```string```  | Código de verificação da nota fiscal |
