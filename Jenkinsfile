pipeline {
    agent any
    
    triggers {
        bitbucketPush()
    }
    
    stages {
        stage ("Pull Code"){
            steps{
                checkout scm
            }
        }

        stage ("Notify Bitbucket"){
            steps{
                bitbucketStatusNotify(
                        buildState: 'INPROGRESS',
                )
                echo "InProgress notification sent successfully!"
            }
        }

        stage('Unit tests') {
            steps {
                sh  '''
                        . /home/ubuntu/venv/bin/activate
                        python -m pytest app/tests/ -v --disable-warnings --junitxml=app/tests/unit_test_results.xml
                    '''
            }
            post {

                always {
                    // Archive unit tests for the future
                    junit (allowEmptyResults: true,
                          testResults: 'app/tests/unit_test_results.xml')
                }
                failure {
                    bitbucketStatusNotify(
                            buildState: 'FAILED',
                    )
                }
            }
        }
        
        stage('Flake8 Analysis') {
            steps {
                echo "Running Flake8 Analysis ..."
                sh  '''
                        . /home/ubuntu/venv/bin/activate
                        flake8 --ignore F401,F403,F405,E731,W605,E722,E501 --output-file flake8_results.txt
                        flake8_junit flake8_results.txt flake8_results_junit.xml
                    '''
            }
            post{
                always{
                    echo "Flake8 Code Analysis Complpeted. Posting results to bitbucket..."
                    junit (allowEmptyResults: true,
                          testResults: 'flake8_results_junit.xml')
                }
                failure {
                    bitbucketStatusNotify(
                            buildState: 'FAILED',
                    )
                }
            }
        }        
    }

    post {
        success {
            bitbucketStatusNotify(
                    buildState: 'SUCCESSFUL',
            )
        }
        failure {
            bitbucketStatusNotify(
                    buildState: 'FAILED',
            )
        }
    }
}