from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import os
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class Summarize(View):
    def post(self, request):
        text = request.POST.get('prompt')
        model = AutoModelForSeq2SeqLM.from_pretrained(os.path.join(os.getcwd(), "summarize/trained_model"))
        tokenizer = AutoTokenizer.from_pretrained(os.path.join(os.getcwd(), "summarize/trained_model"))
        # Encode the input text
        inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)

        # Generate the summary (set max_length to control the length of the summary)
        summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4,
                                     early_stopping=True)

        # Decode and print the summary
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return HttpResponse(summary)
