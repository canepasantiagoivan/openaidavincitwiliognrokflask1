import pandas as pd
import os
import openai
import numpy as np
openai.organization = "org-kdur884nIzDamK0XVxlZA7e1"
openai.api_key = "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"
import numpy as np




def get_embedding(model: str, text: str) -> list[float]:
    result = openai.Embedding.create(
      model = model,
      input = text
    )
    return result['data'][0]['embedding']




tabla['embedding'] = tabla['embedding'].apply(eval).apply(np.array)

print(tabla.head())
