datasets = [
    [
        dict(
            abbr='squad2.0_4',
            eval_cfg=dict(
                evaluator=dict(type='opencompass.datasets.SQuAD20Evaluator'),
                pred_role='BOT'),
            infer_cfg=dict(
                inferencer=dict(
                    max_out_len=50,
                    type='opencompass.openicl.icl_inferencer.GenInferencer'),
                prompt_template=dict(
                    template=dict(round=[
                        dict(
                            prompt=
                            '{context}\nAccording to the above passage, answer the following question. If it is impossible to answer according to the passage, answer `impossible to answer`:\nQuestion: {question}',
                            role='HUMAN'),
                        dict(prompt='Answer:', role='BOT'),
                    ]),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                retriever=dict(
                    type='opencompass.openicl.icl_retriever.ZeroRetriever')),
            path='./data/SQuAD2.0/dev-v2.0.json',
            reader_cfg=dict(
                input_columns=[
                    'context',
                    'question',
                ],
                output_column='answers',
                test_range='[7916:9895]'),
            type='opencompass.datasets.SQuAD20Dataset'),
    ],
]
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
work_dir = './outputs/default/20241011_125436'
