import transformers


processor = transformers.WhisperProcessor(transformers.WhisperFeatureExtractor, transformers.WhisperTokenizer)

