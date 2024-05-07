tokenizer = BertTokenizer.from_pretrained(
    BERT_MODEL,
    do_lower_case=CASED,
    never_split = ("[UNK]", "[SEP]", "[PAD]", "[CLS]", "[MASK]", "[A]", "[B]", "[P]")
)
# These tokens are not actually used, so we can assign arbitrary values.
tokenizer.vocab["[A]"] = -1
tokenizer.vocab["[B]"] = -1
tokenizer.vocab["[P]"] = -1