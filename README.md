# AWS_MLS_Prep
Notes for the AWS Machine learning Speciality Certification


## Resource Compilation
* https://aws.amazon.com/training/learning-paths/machine-learning/exam-preparation/

* https://developers.google.com/machine-learning/crash-course

* https://medium.com/@cjsandeep7/everything-you-need-to-know-about-the-aws-machine-learning-exam-and-your-guide-to-passing-it-b71b6d4d213f
* https://www.reddit.com/r/AWSCertifications/comments/g9otla/just_passed_the_aws_machine_learning_specialty/
* https://www.whizlabs.com/aws-certified-machine-learning-specialty/
* https://www.reddit.com/r/AWSCertifications/comments/gpuj22/aws_machine_learning_zxam_question/
* https://towardsdatascience.com/five-tips-for-passing-the-aws-machine-learning-specialty-exam-a2977654d324




## Topics People mentioned where covered
 * ML algorithms (review/understand every AWS built-in algorithms as for what each of them is for in specific use case is highly recommended)
 *  Hyperparameters tuning
 * security
 * ROC/AUC
 * confusion matrix (3x3)  (Precision/recall/accuracy/f1)
 * Big data services (EMR, Spark, Kinesis)
 *  Bayesian Algo, Statistical
 *  DeepAR is the algorithm that AWS uses for Time Series analysis, BlazeText for NLP
 *  Glue, Kinesis Streams, Analytics, Firehose, S3, IAM, Security, VPC endpoints, EMR - I just had to review/learn other services as Batch, Glue Crawler, Data Pipeline


 - Try to understand what happens when you create a Notebook with Sagemaker. Which infrastructure is created? Which permissions? How do you access training data? How can you share the notebook with other users?

- Differences between Glue, Data Pipeline, Batch: https://cdn.ttgtmedia.com/rms/onlineImages/aws-compare_aws_glue_data_pipeline_batch.png

- When and how can you use CloudWatch? Which events does it log or capture? Where are those captured?

- All about how EMR / Dockerization is used behind the scenes to provision training/serving jobs. For training, where is training data uploaded? which format is supported? which format is supported for better performance? For serving, where are artifafcts stored?

- How endpoints for prediction work. Load Balancing, Production Variants.
* AWS Comprehend
* AWS Transcribe
* Lambda for ml
* AWS SQS
