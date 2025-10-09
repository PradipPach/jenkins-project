pipeline {
agent any

stages {
    stage('Checkout') {
        steps {
            echo "Checking out code..."
            checkout scm
        }
    }

    stage('Setup Python (Amazon Linux)') {
        steps {
            echo "Setting up Python environment on Amazon Linux..."
            sh '''
                echo "Checking Python version..."
                if ! command -v python3 >/dev/null 2>&1; then
                    echo "Python3 not found, installing..."
                    yum install -y python3
                else
                    python3 --version
                fi

                echo "Checking pip installation..."
                if ! command -v pip3 >/dev/null 2>&1; then
                    echo "pip3 not found, installing..."
                    yum install -y python3-pip
                else
                    pip3 --version
                fi

                echo "Upgrading pip..."
                pip3 install --upgrade pip
            '''
        }
    }

    stage('Run Script') {
        steps {
            echo "Running HelloWorld script..."
            sh 'python3 helloworld.py'
        }
    }
}

post {
    success {
        echo "✅ Pipeline completed successfully on Amazon Linux!"
    }
    failure {
        echo "❌ Pipeline failed. Check logs for details."
    }
}


}
