datasets = [
    [
        dict(
            abbr='TheoremQA',
            eval_cfg=dict(
                evaluator=dict(
                    type='opencompass.openicl.icl_evaluator.AccEvaluator'),
                pred_postprocessor=dict(
                    type='opencompass.datasets.TheoremQA_postprocess')),
            infer_cfg=dict(
                inferencer=dict(
                    max_out_len=512,
                    type='opencompass.openicl.icl_inferencer.GenInferencer'),
                prompt_template=dict(
                    template=dict(round=[
                        dict(
                            prompt=
                            'You are a mathematician, you are supposed to answer the given question. You need to output the answer in your final sentence like "Therefore, the answer is ...". The answer can only be one of the following forms:\n1. a numerical value like 0.1, no symbol and no unit at all.\n2. a list of number like [2, 3, 4].\n3. True/False.\n4. an option like (a), (b), (c), (d)\nQuestion: {Question}\nLet\'s think step by step.',
                            role='HUMAN'),
                    ]),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                retriever=dict(
                    type='opencompass.openicl.icl_retriever.ZeroRetriever')),
            path='./data/TheoremQA/test.csv',
            reader_cfg=dict(
                input_columns=[
                    'Question',
                    'Answer_type',
                ],
                output_column='Answer',
                train_split='test'),
            type='opencompass.datasets.TheoremQADataset'),
        dict(
            abbr='mbpp',
            eval_cfg=dict(
                evaluator=dict(type='opencompass.datasets.MBPPEvaluator'),
                pred_role='BOT'),
            infer_cfg=dict(
                inferencer=dict(
                    max_out_len=512,
                    type='opencompass.openicl.icl_inferencer.GenInferencer'),
                prompt_template=dict(
                    template=dict(round=[
                        dict(
                            prompt=
                            'You are an expert Python programmer, and here is your task: Write a function to find the similar elements from the given two tuple lists. Your code should pass these tests:\n\n assert similar_elements((3, 4, 5, 6),(5, 7, 4, 10)) == (4, 5)\n assert similar_elements((1, 2, 3, 4),(5, 4, 3, 7)) == (3, 4) \n assert similar_elements((11, 12, 14, 13),(17, 15, 14, 13)) == (13, 14) \n',
                            role='HUMAN'),
                        dict(
                            prompt=
                            "[BEGIN]\n 'def similar_elements(test_tup1, test_tup2):\r\n  res = tuple(set(test_tup1) & set(test_tup2))\r\n  return (res)' \n[DONE] \n\n ",
                            role='BOT'),
                        dict(
                            prompt=
                            'You are an expert Python programmer, and here is your task: Write a python function to identify non-prime numbers. Your code should pass these tests:\n\n assert is_not_prime(2) == False \n assert is_not_prime(10) == True \n assert is_not_prime(35) == True \n',
                            role='HUMAN'),
                        dict(
                            prompt=
                            "[BEGIN]\n 'import math\r\ndef is_not_prime(n):\r\n    result = False\r\n    for i in range(2,int(math.sqrt(n)) + 1):\r\n        if n % i == 0:\r\n            result = True\r\n    return result' \n[DONE] \n\n ",
                            role='BOT'),
                        dict(
                            prompt=
                            'You are an expert Python programmer, and here is your task: Write a function to find the largest integers from a given list of numbers using heap queue algorithm. Your code should pass these tests:\n\n assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65] \n assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],2)==[85, 75] \n assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35] \n',
                            role='HUMAN'),
                        dict(
                            prompt=
                            "[BEGIN]\n 'import heapq as hq\r\ndef heap_queue_largest(nums,n):\r\n  largest_nums = hq.nlargest(n, nums)\r\n  return largest_nums' \n[DONE] \n\n ",
                            role='BOT'),
                        dict(
                            prompt=
                            'You are an expert Python programmer, and here is your task: {text} Your code should pass these tests:\n\n {test_list}  \n',
                            role='HUMAN'),
                        dict(prompt='[BEGIN]\n', role='BOT'),
                    ]),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                retriever=dict(
                    type='opencompass.openicl.icl_retriever.ZeroRetriever')),
            path='./data/mbpp/mbpp.jsonl',
            reader_cfg=dict(
                input_columns=[
                    'text',
                    'test_list',
                ],
                output_column='test_list_2'),
            type='opencompass.datasets.MBPPDataset'),
        dict(
            abbr='cmmlu-professional_law',
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
                                    '以下是关于专业法学的单项选择题，请直接给出正确答案的选项。\n题目：{question}\nA. {A}\nB. {B}\nC. {C}\nD. {D}',
                                    role='HUMAN'),
                                dict(prompt='答案是: A', role='BOT'),
                            ]),
                        B=dict(
                            begin='</E>',
                            round=[
                                dict(
                                    prompt=
                                    '以下是关于专业法学的单项选择题，请直接给出正确答案的选项。\n题目：{question}\nA. {A}\nB. {B}\nC. {C}\nD. {D}',
                                    role='HUMAN'),
                                dict(prompt='答案是: B', role='BOT'),
                            ]),
                        C=dict(
                            begin='</E>',
                            round=[
                                dict(
                                    prompt=
                                    '以下是关于专业法学的单项选择题，请直接给出正确答案的选项。\n题目：{question}\nA. {A}\nB. {B}\nC. {C}\nD. {D}',
                                    role='HUMAN'),
                                dict(prompt='答案是: C', role='BOT'),
                            ]),
                        D=dict(
                            begin='</E>',
                            round=[
                                dict(
                                    prompt=
                                    '以下是关于专业法学的单项选择题，请直接给出正确答案的选项。\n题目：{question}\nA. {A}\nB. {B}\nC. {C}\nD. {D}',
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
            name='professional_law',
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
work_dir = './outputs/default/20241009_162539'
