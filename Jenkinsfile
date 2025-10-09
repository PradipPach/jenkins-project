pipeline {
agent any

stages {
    stage('Checkout') {
        steps {
            echo "Checking out code..."
            checkout scm
        }
    }

    stage('Setup Python') {
        steps {
            echo "Setting up Python environment..."
            sh '''
                echo "Checking Python version..."
                python3 --version

                echo "Checking pip installation..."
                if ! command -v pip3 >/dev/null 2>&1; then
                    echo "pip3 not found. Installing..."
                    apt update -y && apt install -y python3-pip
                else
                    echo "pip3 already installed."
                fi

                echo "Verifying pip3 version..."
                pip3 --version
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
        echo "✅ Pipeline completed successfully!"
    }
    failure {
        echo "❌ Pipeline failed. Check logs."
    }
}


}
