-> Ambiente
git clone https://github.com/eubr-bigsea/docker-lemonade.git
cd docker-lemonade

git submodule update --init --checkout

cd <MODULO>
git checkout master

cd thorn
nano requirements.txt
adicionar greenlet==0.4.15

Adicionar no docker-compose.yml

adminer:
    image: adminer:4.7.5-standalone
    restart: always
    ports:
      - 8080:8080
    environment:
      - ADMINER_DEFAULT_SERVER=mysql
    depends_on:
      - mysql

cd tahiti
Editar requirements.txt com werkzeug 0.15.5

#fora do tahiti
docker-compose up -d --build
docker-compose down
docker-compose up -d mysql
docker-compose up -d redis
docker-compose up -d adminer
docker-compose up -d

login:
admin@lemonade.org.br
senha:
admin

-> Migration Tahiti:
sudo pip install virtualenv
virtualenv <NOME>
source <NOME>/bin/activate

cd docker-lemonade
cd tahiti
pip install -r requirements.txt

PYTHONPATH=. TAHITI_CONFIG=../config/tahiti-config.yaml python3 tahiti/manage.py db revision -m "mpce"

-> Adminer

localhost:8080
login:root
senha:lemon


-> Templates:

/home//Projetos/Unifor/mpce/docker-lemonade/tahiti/migrations/versions/4b5b8e3470af_update_sklearn_operations.py

/home//Projetos/Unifor/mpce/docker-lemonade/tahiti/migrations/versions/6c6668dd3682_add_dbscan_clustering_operation_scikit_.py

-> Transpiler Juicer:
docker-lemonade/juicer/juicer/scikit_learn/transpiler.py
docker-lemonade/juicer/juicer/scikit_learn/clustering_operation.py.py

docker-compose down
sudo rm -rf /srv/lemonade/*

docker-compose up -d --build
docker-compose down
docker-compose up -d mysql
docker-compose up -d redis
docker-compose up -d adminer
docker-compose up -d

docker-compose up -d --build worker

docker-compose exec <CONTAINER> sh

scp /home//Downloads/Image-20210419T204943Z-001.zip login@10.1.1.112:/home//files/Image-20210419T204943Z-001.zip
scp /home/danielvmacedo/Downloads/extract_frames.py daniel.macedo@10.1.1.112:/home/daniel.macedo/files/extract_frames.py
scp daniel.macedo@10.1.1.112:/home/daniel.macedo/files/daniel/mpce_dataset.pkl /home/danielvmacedo/Downloads/mpce_dataset.pkl
scp daniel.macedo@10.1.1.112:/home/daniel.macedo/files/daniel/mpce_dataset.pkl /home/danielvmacedo/Downloads/mpce_dataset.pkl

-> Dúvidas:
storage_folder = "/srv/storage/srv/storage/limonero/data/"

Operations Type: TRANSFORMATION, ACTION, VISUALIZATION??

Executar fluxos de forma automatizada


curl 'localhost:8000/api/v1/stand/workflow?2&api_token=MlRGKU8JVfdzTIi' -X POST -H 'Content-type: application/json' -d '{"workflow_id": 1, "cluster_id": 1}'

Adicionar:
tahiti:
            url: http://tahiti:23403
            auth_token: '123456'

no stand-config

python juicer/app.py -c ../juicer-config.yaml -w 1

python juicer/runner/minion.py -c ../config/juicer-config.yaml -w 2 -t scikit-learn

python juicer/runner/server.py -c ../config/juicer-config.yaml

emit_event(
                   'update task', status='COMPLETED',
                   identifier='{task_id}',
                   message=content.generate(),
                   type='HTML', title='Evaluation result',
                   task={{'id': '{task_id}'}},
                   operation={{'id': {operation_id}}},
                   operation_id={operation_id})


emit_event(
                            'update task', status='COMPLETED',
                            identifier='{task_id}',
                            message=base64.b64encode(fig_file.getvalue()),
                            type='IMAGE', title='{title}',
                            task={{'id': '{task_id}'}},
                            operation={{'id': {operation_id}}},
                            operation_id={operation_id})


https://paperswithcode.com/paper/ava-activespeaker-an-audio-visual-dataset-for

def generate_code(self):
        if self.has_code:
            code = [dedent(get_caipirinha_config(self.config)),
            dedent("""
            {out} = None
            #MPCE
            from juicer.service import caipirinha_service
            from juicer.scikit_learn.vis_operation import HtmlVisualizationModel

            visualization = {{
                    'job_id': '{job_id}',
                    'task_id': '{task_id}',
                    'title': '{title}',
                    'type': {{
                        'id': 1,
                        'name': 'HTML'
                    }},
                    'model': HtmlVisualizationModel(title='{title}'),
                    'data': json.dumps({{
                        'html': 'testando <b>html</b> agora'
                    }}),
                }}
            #emit_event(
            #                'update task', status='COMPLETED',
            #                identifier='{task_id}',
            #                message='testando <b>html</b> agora',
            #                type='HTML', title='{title}',
            #                task={{'id': '{task_id}'}},
            #                operation={{'id': {operation_id}}},
            #                operation_id={operation_id})

            caipirinha_service.new_visualization(
                            config,
                            {user},
                            {workflow_id}, {job_id}, '{task_id}',
                            visualization, emit_event)
            """ \
                .format(out=self.output, task_id=self.parameters['task_id'], title=self.title, operation_id=self.parameters['operation_id'], job_id=self.parameters['job_id'], user=self.parameters['user'], workflow_id=self.parameters['workflow_id']))]
            
            return ''.join(code)
            #return dedent(code)

{out} = HtmlVisualizationModel(title='{title}', data=json.dumps({{
                        'html': 'Teste <b>oi<b> Teste'
                    }}))
            

            visualization = {{
                    'job_id': '{job_id}',
                    'task_id': '{task_id}',
                    'title': '{title}',
                    'type': {{
                        'id': 1,
                        'name': 'HTML'
                    }},
                    'model': {out},
                    'data': json.dumps({{
                        'html': 'Teste <b>oi<b> Teste'
                    }}),
                }}
            {out} = visualization

{out} = HtmlVisualizationModel(type_name='HTML', type_id='1', task_id='{task_id}', title='{title}', data=json.dumps({{
                        'html': 'Teste <b>oi<b> Teste'
                    }}))

            visualization = {{
                    'job_id': '{job_id}',
                    'task_id': '{task_id}',
                    'title': '{title}',
                    'type': {{
                        'id': 1,
                        'name': 'HTML'
                    }},
                    'model': {out},
                    'data': json.dumps({{
                        'html': 'testando <b>html</b> agora'
                    }}),
                }}


[83, [{"en": "CSV data file", "value": "CSV data file", "key": "CSV",
               "pt": "Arquivo de dados CSV"},
              {"en": "JSON data file", "value": "JSON data file", "key": "JSON",
               "pt": "Arquivo de dados JSON"},
              {"en": "Parquet data file", "value": "Parquet data file",
               "key": "PARQUET", "pt": "Arquivo de dados Parquet"}]],    

img = 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
