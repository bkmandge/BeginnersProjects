# Proofreading Text
import lmproof

def proofread(text):
    proofread = lmproof.load("en")
    corrected_str = proofread.proofread(text)
    print(f"Original Text: {text}")
    print(f"Corrected Text: {corrected_str}")


proofread('Enter the text:')