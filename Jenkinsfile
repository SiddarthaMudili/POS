pipeline {
  agent {
    label 'docker-agent'
  }

  environment {
    DOCKER_IMAGE = 'flask-app'
  }

  stages {
    stage('Checkout Code') {
      steps {
        git 'https://github.com/SiddarthaMudili/POS.git'
      }
    }
    
    stage('Authenticate for Sudo') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'sudo-creds', usernameVariable: 'SUDO_USER', passwordVariable: 'SUDO_PASS')]) {
          script {
            // Save sudo password to a temporary file with restricted permissions
            writeFile file: 'sudo_pass.sh', text: "#!/bin/bash\necho \"${SUDO_PASS}\""
            sh 'chmod 700 sudo_pass.sh'
          }
        }
      }
    }

    stage('Remove Old Container') {
      steps {
        script {
          sh './sudo_pass.sh | sudo -S docker compose down || true'
        }
      }
    }

    stage('Deploy Container') {
      steps {
        sh './sudo_pass.sh | sudo -S docker compose up -d'
      } 
    }

    stage('Clean Up') {
      steps {
        sh 'rm -f sudo_pass.sh'
      }
    }
  }
}
