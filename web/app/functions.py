# from mailjet_rest import Client


# def enviar_email(destinatarios, template_id, asunto, variables, adjuntos):
#     # "Variables": {
#     #                 "titulo": titulo,
#     #                 "body": body,
#     #                 "btn_mail": '<a href="' + url_btn + '" style="background-color: #015fc9; border-radius: 30px;   color: white;   padding: 15px 32px;   text-align: center;   text-decoration: none;   display: inline-block;   font-size: 16px;">' + text_btn + '</a>'
#     #             },
#     api_key = '51844bc4a2b1ceaa85b611b0330a43df'
#     api_secret = '5c73bfc938276efc3ec4921455ac2ac5'
#     mailjet = Client(auth=(api_key, api_secret), version='v3.1')
#     data = {
#     'Messages': [
#             {
#                 "From": {
#                     "Email": "contacto@sparemotors.cl",
#                     "Name": "Contacto Spare Motors"
#                 },
#                 "To": destinatarios,
#                 "TemplateID": template_id,
#                 "TemplateLanguage": True,
#                 "Subject": asunto,
#                 "Variables": variables,
#                 "Attachments": adjuntos
#             }
#         ]
#     }
#     result = mailjet.send.create(data=data)
#     print(result.status_code)
#     print(result.json())