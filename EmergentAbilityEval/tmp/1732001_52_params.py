datasets = [
    [
        dict(
            abbr='triviaqa_5shot_4',
            eval_cfg=dict(
                evaluator=dict(type='opencompass.datasets.TriviaQAEvaluator'),
                pred_role='BOT'),
            infer_cfg=dict(
                ice_template=dict(
                    template=dict(round=[
                        dict(
                            prompt=
                            "Answer the question, your answer should be as simple as possible, start your answer with the prompt 'The answer is '.\nQ: {question}?",
                            role='HUMAN'),
                        dict(
                            prompt='A: The answer is {answer}.\n', role='BOT'),
                    ]),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                inferencer=dict(
                    max_out_len=50,
                    type='opencompass.openicl.icl_inferencer.GenInferencer'),
                prompt_template=dict(
                    ice_token='</E>',
                    template=dict(
                        begin='</E>',
                        round=[
                            dict(
                                prompt=
                                "Answer the question, your answer should be as simple as possible, start your answer with the prompt 'The answer is '.\nQ: {question}?",
                                role='HUMAN'),
                            dict(prompt='A:', role='BOT'),
                        ]),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                retriever=dict(
                    fix_id_list=[
                        0,
                        1,
                        2,
                        3,
                        4,
                    ],
                    type='opencompass.openicl.icl_retriever.FixKRetriever')),
            path='./data/triviaqa/',
            reader_cfg=dict(
                input_columns=[
                    'question',
                ],
                output_column='answer',
                test_range='[7072:8840]',
                test_split='dev',
                train_split='test'),
            type='opencompass.datasets.TriviaQADataset'),
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
