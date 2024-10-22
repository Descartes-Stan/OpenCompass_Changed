datasets = [
    [
        dict(
            abbr='siqa',
            eval_cfg=dict(
                evaluator=dict(
                    type='opencompass.openicl.icl_evaluator.AccEvaluator')),
            infer_cfg=dict(
                inferencer=dict(
                    type='opencompass.openicl.icl_inferencer.PPLInferencer'),
                prompt_template=dict(
                    template=dict({
                        '1':
                        dict(round=[
                            dict(
                                prompt=
                                '{context}\nQuestion: {question}\nA. {answerA}\nB. {answerB}\nC. {answerC}',
                                role='HUMAN'),
                            dict(prompt='Answer: A', role='BOT'),
                        ]),
                        '2':
                        dict(round=[
                            dict(
                                prompt=
                                '{context}\nQuestion: {question}\nA. {answerA}\nB. {answerB}\nC. {answerC}',
                                role='HUMAN'),
                            dict(prompt='Answer: B', role='BOT'),
                        ]),
                        '3':
                        dict(round=[
                            dict(
                                prompt=
                                '{context}\nQuestion: {question}\nA. {answerA}\nB. {answerB}\nC. {answerC}',
                                role='HUMAN'),
                            dict(prompt='Answer: C', role='BOT'),
                        ])
                    }),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                retriever=dict(
                    type='opencompass.openicl.icl_retriever.ZeroRetriever')),
            path='./data/siqa',
            reader_cfg=dict(
                input_columns=[
                    'context',
                    'question',
                    'answerA',
                    'answerB',
                    'answerC',
                ],
                output_column='label',
                test_split='validation'),
            type='opencompass.datasets.siqaDataset'),
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
work_dir = './outputs/default/20241009_104207'
