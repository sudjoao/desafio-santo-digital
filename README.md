# Intership Challenge SantoDigital

## Sobre
Desenvolvimento de uma API que retorne campos específicos de uma NF a partir do JSON fornecido pelo Google Vision API.

## Rodar localmente
### Instalações

#### 1. [Python]()
#### 2. [a]()

### Execução
##### 1. Entrar na pasta raiz
```
cd Desafio/
```
#### 2. Configurar o ambiente
```
python3 -m venv venv
. venv/bin/activate
pip install Flask
```
#### 3. Exportar variavél de ambiente
```
export FLASK_APP=project/views/main.py
```
#### 4. Rodar o servidor
```
flask run
```
<br>
<br>

#  Rotas

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