pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Brajbrishti/BASIC.git'
            }
        }
        

	stage ('Code is being execute !'){
	    steps {		
		bat "code done"
	}}
        stage('Run Python Script') {
            steps {
                bat 'python Python\\triangle.py'
            }
        }
    }
}
