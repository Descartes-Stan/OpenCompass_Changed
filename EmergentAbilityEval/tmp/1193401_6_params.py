datasets = [
    [
        dict(
            abbr='ARC-c',
            eval_cfg=dict(
                evaluator=dict(
                    type='opencompass.openicl.icl_evaluator.AccEvaluator')),
            infer_cfg=dict(
                inferencer=dict(
                    type='opencompass.openicl.icl_inferencer.PPLInferencer'),
                prompt_template=dict(
                    template=dict(
                        A=dict(round=[
                            dict(
                                prompt=
                                '{question}\nA. {textA}\nB. {textB}\nC. {textC}\nD. {textD}',
                                role='HUMAN'),
                            dict(prompt='Answer: A', role='BOT'),
                        ]),
                        B=dict(round=[
                            dict(
                                prompt=
                                '{question}\nA. {textA}\nB. {textB}\nC. {textC}\nD. {textD}',
                                role='HUMAN'),
                            dict(prompt='Answer: B', role='BOT'),
                        ]),
                        C=dict(round=[
                            dict(
                                prompt=
                                '{question}\nA. {textA}\nB. {textB}\nC. {textC}\nD. {textD}',
                                role='HUMAN'),
                            dict(prompt='Answer: C', role='BOT'),
                        ]),
                        D=dict(round=[
                            dict(
                                prompt=
                                '{question}\nA. {textA}\nB. {textB}\nC. {textC}\nD. {textD}',
                                role='HUMAN'),
                            dict(prompt='Answer: D', role='BOT'),
                        ])),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                retriever=dict(
                    type='opencompass.openicl.icl_retriever.ZeroRetriever')),
            path='./data/ARC/ARC-c/ARC-Challenge-Dev.jsonl',
            reader_cfg=dict(
                input_columns=[
                    'question',
                    'textA',
                    'textB',
                    'textC',
                    'textD',
                ],
                output_column='answerKey'),
            type='opencompass.datasets.ARCDataset'),
    ],
]
eval = dict(runner=dict(task=dict()))
models = [
    dict(
        abbr='hf_llama-7b',
        batch_padding=False,
        batch_size=16,
        max_out_len=100,
        max_seq_len=2048,
        model_kwargs=dict(device_map='auto', trust_remote_code=True),
        path='huggyllama/llama-7b',
        run_cfg=dict(num_gpus=1, num_procs=1),
        tokenizer_kwargs=dict(
            padding_side='left',
            truncation_side='left',
            trust_remote_code=True,
            use_fast=False),
        tokenizer_path='huggyllama/llama-7b',
        type='opencompass.models.HuggingFaceCausalLM'),
]
work_dir = './outputs/default/20241009_102005'
