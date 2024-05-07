# Model
bert_model = "bert-large-cased"
n_bertlayers = 22
dropout = 0.1

# Preprocessing
do_lower_case = False

# Training
train_batch_size = 4
gradient_accumulation_steps = 5
lr = 1e-5
num_train_epochs = 2
warmup_proportion = 0.1
optim = "bertadam"
weight_decay = False


# Others
n_models = 10
eval_batch_size = 32

device = torch.device("cuda")
data_dir = ""