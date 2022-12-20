# tweet-winner

In order to run this project on your own, you can just apply the deploy.yaml on your Kubernetes clsuter. You would need to create a secret before applying this with the bearer token. This will deploy all the components in demo namespace. 

You can get the bearer token form [Twitter Developers](https://developer.twitter.com/).

<img width="637" alt="Screenshot 2022-12-20 at 9 40 41 AM" src="https://user-images.githubusercontent.com/8190114/208583643-6e3ea85e-c8f2-4896-baa5-e9a073924944.png">

Create secrets using below command 

'''
kubectl create secret -n demo generic apikey --from-literal=value="Bearer_token"
'''

Make sure you have an ingress controller installed in order to access the ingress created, in this case Traefik ingress controller is used.If not, you can change the service to Loadbalancer or access it via nodeport.


For Developement:

All the code and files are also in the repo, so if you want to customize the html, Dockerfile or code, you can do that. Though contributions to improve are welcome.

Note - the error handling is currenlty not there, so that is something that can be contirbuted first.


