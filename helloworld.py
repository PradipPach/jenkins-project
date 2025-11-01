pipeline { 
     agent any 
  
     stages { 
         stage('dev') { 
             steps { 
                 echo 'I am in dev' 
                 sh 'git --version' 
             } 
         } 
         stage('test') { 
             steps { 
                 echo 'I am in test' 
                 sh 'docker --version' 
             } 
         } 
         stage('prod') { 
             steps { 
                 echo 'I am in prod' 
                 sh 'pwd' 
                 sh 'git init' 
             } 
         } 
     } 
 }
