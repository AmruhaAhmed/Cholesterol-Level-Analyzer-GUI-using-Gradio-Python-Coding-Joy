! pip install gradio
#installing gradio
import gradio as gr#importing gradio library
#creating a function cholcheck that accepts total_cholesterol,ldl_cholesterol,hdl_cholesterol,triglycerides as parameters in terms of mg/dL

def cholcheck(total_cholesterol,ldl_cholesterol,hdl_cholesterol,triglycerides):
  #interpreting cholestrol test values
  if(total_cholesterol<200 and ldl_cholesterol<130 and hdl_cholesterol>50 and triglycerides<200):
    return("Ideal Level of cholesterol")
  elif((total_cholesterol>=200 and total_cholesterol<=239) and (ldl_cholesterol>=130 and ldl_cholesterol<=159) and (hdl_cholesterol>=40 and hdl_cholesterol<=49) and (triglycerides>200 and triglycerides<=399)):
    return("Borderline High Level of Cholesterol detected")
  else:
    return("High Levels of Cholesterol detected")

interface=gr.Interface(fn=cholcheck,inputs=["number","number","number","number"],outputs=['text'],title="CHOLESTROL TEST ANALYSER")
interface.launch()