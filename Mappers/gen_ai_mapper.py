from Instructions.GenerativeAI.vectordb import vectordb
from Instructions.GenerativeAI.rag import rag
from Instructions.GenerativeAI.gans import gan_explanation
from Instructions.GenerativeAI.vae import vae_markdown
from Instructions.GenerativeAI.interview_q import generative_ai_interview
from Instructions.GenerativeAI.foundation_model import foundation_model_explanation


GENAI_MAPPER = {
    "Foundation Model": [foundation_model_explanation, './Instructions/GenerativeAI/foundation.png'],
    "Vector Database": [vectordb, './Instructions/GenerativeAI/vectordb.png'],
    "Generative Adversarial Networks": [gan_explanation, './Instructions/GenerativeAI/gans.png'],
    "Variational Autoencoders": [vae_markdown, './Instructions/GenerativeAI/vae.png'],
    "Retrieval Augmented Generation": [rag, './Instructions/GenerativeAI/rag.png'],
    "Inteview Question": [generative_ai_interview, './Instructions/GenerativeAI/genaiint.png'],
}
