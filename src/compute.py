import time


def run(self):
    print("start")
    time.sleep(5)
    print(self.request)
    print("done")

# # return flask forms as dict
# data = request.form

# #  sms or mms - zero indicates sms
# flag = str(data["NumMedia"])

# #  gcs bucket name - images saved here
# bucket_name = "twillio-images"

# # required to initialize vertex client
# project = "cf-data-analytics"
# loc = "us-central1"

# # process multimedia messages (mms)
# if flag != "0":

#     # download image from twillio
#     mms_process(data)

#     #  set filename of images sent to gcs. Use unique identifier from twillio
#     filename = data["SmsSid"] + ".png"

#     # Upload image to gcs bucket
#     upload_blob(bucket_name, filename, filename)

#     # save metadata to firestore collection 1 (filename, masked identifier)
#     save_results_collection1(
#         data["SmsSid"], number_mask(data["From"]), filename)

#     # create results doc
#     save_results_collection2(data["SmsSid"], filename)

# # process text messages
# else:

#     #  retrieve last image URL uploaded by same user from Firestore
#     time.sleep(5)
#     doc = return_image(number_mask(data["From"]))
#     filename = doc["fileName"]

#     # construct gsl using filename
#     path = "gs://" + bucket_name + "/" + filename  # uri

#     # genrate response using gemini
#     genai_ouput = generate_text(
#         project, loc, path, data["Body"])

#     print(genai_ouput)

#     update_collection2(doc["fileName"].split(
#         ".")[0], data["Body"], genai_ouput)

# #  debug: print entire payload from twillio
# # myJSON = json.dumps(data)
# # print(myJSON)

# except Exception as e:
# print(e)