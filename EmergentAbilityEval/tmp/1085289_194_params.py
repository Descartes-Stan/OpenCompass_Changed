datasets = [
    [
        dict(
            abbr='cmmlu-virology',
            eval_cfg=dict(
                evaluator=dict(
                    type='opencompass.openicl.icl_evaluator.AccEvaluator')),
            infer_cfg=dict(
                ice_template=dict(
                    ice_token='</E>',
                    template=dict(
                        A=dict(
                            begin='</E>',
                            round=[
                                dict(
                                    prompt=
                                    '以下是关于病毒学的单项选择题，请直接给出正确答案的选项。\n题目：{question}\nA. {A}\nB. {B}\nC. {C}\nD. {D}',
                                    role='HUMAN'),
                                dict(prompt='答案是: A', role='BOT'),
                            ]),
                        B=dict(
                            begin='</E>',
                            round=[
                                dict(
                                    prompt=
                                    '以下是关于病毒学的单项选择题，请直接给出正确答案的选项。\n题目：{question}\nA. {A}\nB. {B}\nC. {C}\nD. {D}',
                                    role='HUMAN'),
                                dict(prompt='答案是: B', role='BOT'),
                            ]),
                        C=dict(
                            begin='</E>',
                            round=[
                                dict(
                                    prompt=
                                    '以下是关于病毒学的单项选择题，请直接给出正确答案的选项。\n题目：{question}\nA. {A}\nB. {B}\nC. {C}\nD. {D}',
                                    role='HUMAN'),
                                dict(prompt='答案是: C', role='BOT'),
                            ]),
                        D=dict(
                            begin='</E>',
                            round=[
                                dict(
                                    prompt=
                                    '以下是关于病毒学的单项选择题，请直接给出正确答案的选项。\n题目：{question}\nA. {A}\nB. {B}\nC. {C}\nD. {D}',
                                    role='HUMAN'),
                                dict(prompt='答案是: D', role='BOT'),
                            ])),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                inferencer=dict(
                    type='opencompass.openicl.icl_inferencer.PPLInferencer'),
                retriever=dict(
                    fix_id_list=[
                        0,
                        1,
                        2,
                        3,
                        4,
                    ],
                    type='opencompass.openicl.icl_retriever.FixKRetriever')),
            name='virology',
            path='./data/cmmlu/',
            reader_cfg=dict(
                input_columns=[
                    'question',
                    'A',
                    'B',
                    'C',
                    'D',
                ],
                output_column='answer',
                test_split='test',
                train_split='dev'),
            type='opencompass.datasets.CMMLUDataset'),
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
work_dir = './outputs/default/20241008_231138'
