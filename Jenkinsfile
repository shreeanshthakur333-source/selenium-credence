pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Run Python') {
      steps {
        script {
          if (isUnix()) {
            sh 'python3 -V || python -V'
            sh 'python3 main.py || python main.py'
          } else {
            bat 'python -V'
            bat 'python main.py'
          }
        }
      }
    }
  }
}