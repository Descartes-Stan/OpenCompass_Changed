datasets = [
    [
        dict(
            abbr='nq_0',
            eval_cfg=dict(
                evaluator=dict(type='opencompass.datasets.NQEvaluator'),
                pred_role='BOT'),
            infer_cfg=dict(
                inferencer=dict(
                    max_out_len=50,
                    type='opencompass.openicl.icl_inferencer.GenInferencer'),
                prompt_template=dict(
                    template=dict(round=[
                        dict(
                            prompt=
                            "Answer these questions, your answer should be as simple as possible, start your answer with the prompt 'The answer is '.\nQ: {question}?",
                            role='HUMAN'),
                        dict(prompt='A:', role='BOT'),
                    ]),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                retriever=dict(
                    type='opencompass.openicl.icl_retriever.ZeroRetriever')),
            path='./data/nq/',
            reader_cfg=dict(
                input_columns=[
                    'question',
                ],
                output_column='answer',
                test_range='[0:1805]',
                train_split='dev'),
            type='opencompass.datasets.NaturalQuestionDataset'),
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
