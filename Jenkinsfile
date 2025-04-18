pipeline {
    agent any

    stages {
        // Etapa 1: Build y despliegue en Desarrollo
        stage('Deploy Desarrollo') {
            steps {
                script {
                    // Clonar repo y construir
                    git 'https://github.com/ch3m4SK/TO-DO-App.git'
                    sh 'docker-compose -f docker-compose.dev.yml build'
                    sh 'docker-compose -f docker-compose.dev.yml up -d'
                }
            }
        }

        // Etapa 2: Esperar aprobación manual
        stage('Aprobar Producción') {
            steps {
                script {
                    // Notificar por Slack/Email (opcional)
                    slackSend channel: '#devops', message: "✅ Desarrollo desplegado. ¿Desplegar en Producción?"
                    
                    // Esperar confirmación humana
                    input message: '¿Desplegar en Producción?', ok: 'Confirmar'
                }
            }
        }

        // Etapa 3: Desplegar en Producción
        stage('Deploy Producción') {
            steps {
                script {
                    // Ejecutar playbook Ansible en VM2
                    ansiblePlaybook(
                        playbook: 'deploy-prod.yml',
                        inventory: 'hosts-prod.ini',
                        credentialsId: 'credenciales-prod'
                    )
                }
            }
        }
    }
}