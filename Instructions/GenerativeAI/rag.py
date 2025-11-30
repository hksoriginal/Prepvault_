rag = r'''
Retrieval Augmented Generation (RAG) combines retrieval-based methods with generative models
to improve the generation process by leveraging external knowledge.

Key Steps in RAG:
1. **Query Encoding**: Convert input into a vector representation using an encoder.
2. **Document Retrieval**: Retrieve relevant documents from a knowledge base.
3. **Text Generation**: Use the retrieved documents to generate a response using a generative model.

RAG Model Modes:
- **RAG-Token**: Retrieves documents for each token during generation.
- **RAG-Sequence**: Retrieves documents once, then generates the full sequence.

Benefits:
- **Improved accuracy** by reducing hallucinations.
- **Access to external knowledge** in real-time.
- **Scalability** to large knowledge bases.
'''
