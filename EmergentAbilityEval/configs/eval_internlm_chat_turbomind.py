from mmengine.config import read_base
from opencompass.models.turbomind import TurboMindModel


with read_base():
    # choose a list of datasets
    from .datasets.mmlu.mmlu_gen_a484b3 import mmlu_datasets
    from .datasets.ceval.ceval_gen_5f30c7 import ceval_datasets
    from .datasets.SuperGLUE_WiC.SuperGLUE_WiC_gen_d06864 import WiC_datasets
    from .datasets.triviaqa.triviaqa_gen_2121ce import triviaqa_datasets
    from .datasets.gsm8k.gsm8k_gen_1d7fe4 import gsm8k_datasets
    from .datasets.humaneval.humaneval_gen_8e312c import humaneval_datasets
    from .datasets.race.race_gen_69ee4f import race_datasets
    from .datasets.crowspairs.crowspairs_gen_381af0 import crowspairs_datasets
    # and output the results in a choosen format
    from .summarizers.medium import summarizer

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])


meta_template = dict(
    round=[
        dict(role='HUMAN', begin='<|User|>:', end='\n'),
        dict(role='BOT', begin='<|Bot|>:', end='<eoa>\n', generate=True),
    ],
    eos_token_id=103028)

# config for internlm-chat-7b
# models = [
#     dict(
#         type=TurboMindModel,
#         abbr='internlm-chat-7b-turbomind',
#         path="./turbomind",
#         max_out_len=100,
#         max_seq_len=2048,
#         batch_size=32,
#         concurrency=32,
#         meta_template=meta_template,
#         run_cfg=dict(num_gpus=1, num_procs=1),
#     )
# ]

# config for internlm-chat-7b-w4 model
# models = [
#     dict(
#         type=TurboMindModel,
#         abbr='internlm-chat-7b-w4-turbomind',
#         path="./turbomind",
#         max_out_len=100,
#         max_seq_len=2048,
#         batch_size=32,
#         concurrency=32,
#         meta_template=meta_template,
#         run_cfg=dict(num_gpus=1, num_procs=1),
#     )
# ]

# config for internlm-chat-7b-w4kv8 model
# models = [
#     dict(
#         type=TurboMindModel,
#         abbr='internlm-chat-7b-w4kv8-turbomind',
#         path="./turbomind",
#         max_out_len=100,
#         max_seq_len=2048,
#         batch_size=32,
#         concurrency=32,
#         meta_template=meta_template,
#         run_cfg=dict(num_gpus=1, num_procs=1),
#     )
# ]

# config for internlm-chat-20b
# models = [
#     dict(
#         type=TurboMindModel,
#         abbr='internlm-chat-20b-turbomind',
#         path="./turbomind",
#         max_out_len=100,
#         max_seq_len=2048,
#         batch_size=8,
#         concurrency=8,
#         meta_template=meta_template,
#         run_cfg=dict(num_gpus=1, num_procs=1),
#     )
# ]

# config for internlm-chat-20b-w4 model
models = [
    dict(
        type=TurboMindModel,
        abbr='internlm-chat-20b-w4-turbomind',
        path="./turbomind",
        max_out_len=100,
        max_seq_len=2048,
        batch_size=16,
        concurrency=16,
        meta_template=meta_template,
        run_cfg=dict(num_gpus=1, num_procs=1),
    )
]

# config for internlm-chat-20b-w4kv8 model
# models = [
#     dict(
#         type=TurboMindModel,
#         abbr='internlm-chat-20b-w4kv8-turbomind',
#         path="./turbomind",
#         max_out_len=100,
#         max_seq_len=2048,
#         batch_size=16,
#         concurrency=16,
#         meta_template=meta_template,
#         run_cfg=dict(num_gpus=1, num_procs=1),
#     )
# ]
