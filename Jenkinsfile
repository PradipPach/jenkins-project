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
                     python3 --version 
                     pip3 --version || sudo apt install python3-pip -y 
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
