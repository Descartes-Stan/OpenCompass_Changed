datasets = [
    [
        dict(
            abbr='math_22',
            eval_cfg=dict(
                evaluator=dict(type='opencompass.datasets.MATHEvaluator'),
                pred_postprocessor=dict(
                    type='opencompass.datasets.math_postprocess')),
            infer_cfg=dict(
                inferencer=dict(
                    max_out_len=512,
                    type='opencompass.openicl.icl_inferencer.GenInferencer'),
                prompt_template=dict(
                    template=dict(round=[
                        dict(
                            prompt=
                            'Problem:\nFind the domain of the expression $\\frac{{\\sqrt{{x-2}}}}{{\\sqrt{{5-x}}}}$.}}\nSolution:',
                            role='HUMAN'),
                        dict(
                            prompt=
                            'The expressions inside each square root must be non-negative. Therefore, $x-2 \\ge 0$, so $x\\ge2$, and $5 - x \\ge 0$, so $x \\le 5$. Also, the denominator cannot be equal to zero, so $5-x>0$, which gives $x<5$. Therefore, the domain of the expression is $\\boxed{{[2,5)}}$.\nFinal Answer: The final answer is $[2,5)$. I hope it is correct.\n',
                            role='BOT'),
                        dict(
                            prompt=
                            'Problem:\nIf $\\det \\mathbf{{A}} = 2$ and $\\det \\mathbf{{B}} = 12,$ then find $\\det (\\mathbf{{A}} \\mathbf{{B}}).$\nSolution:',
                            role='HUMAN'),
                        dict(
                            prompt=
                            'We have that $\\det (\\mathbf{{A}} \\mathbf{{B}}) = (\\det \\mathbf{{A}})(\\det \\mathbf{{B}}) = (2)(12) = \\boxed{{24}}.$\nFinal Answer: The final answer is $24$. I hope it is correct.\n',
                            role='BOT'),
                        dict(
                            prompt=
                            'Problem:\nTerrell usually lifts two 20-pound weights 12 times. If he uses two 15-pound weights instead, how many times must Terrell lift them in order to lift the same total weight?\nSolution:',
                            role='HUMAN'),
                        dict(
                            prompt=
                            'If Terrell lifts two 20-pound weights 12 times, he lifts a total of $2\\cdot 12\\cdot20=480$ pounds of weight. If he lifts two 15-pound weights instead for $n$ times, he will lift a total of $2\\cdot15\\cdot n=30n$ pounds of weight. Equating this to 480 pounds, we can solve for $n$: \\begin{{align*}} 30n&=480\\\\ \\Rightarrow\\qquad n&=480/30=\\boxed{{16}} \\end{{align*}}\nFinal Answer: The final answer is $16$. I hope it is correct.\n',
                            role='BOT'),
                        dict(
                            prompt=
                            'Problem:\nIf the system of equations: \\begin{{align*}} 6x-4y&=a,\\\\ 6y-9x &=b. \\end{{align*}}has a solution $(x, y)$ where $x$ and $y$ are both nonzero, find $\\frac{{a}}{{b}},$ assuming $b$ is nonzero.\nSolution:',
                            role='HUMAN'),
                        dict(
                            prompt=
                            'If we multiply the first equation by $-\\frac{{3}}{{2}}$, we obtain $$6y-9x=-\\frac{{3}}{{2}}a.$$Since we also know that $6y-9x=b$, we have $$-\\frac{{3}}{{2}}a=b\\Rightarrow\\frac{{a}}{{b}}=\\boxed{{-\\frac{{2}}{{3}}}}.$$\nFinal Answer: The final answer is $-\\frac{{2}}{{3}}$. I hope it is correct.\n',
                            role='BOT'),
                        dict(
                            prompt='Problem:\n{problem}\nSolution:\n',
                            role='HUMAN'),
                    ]),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                retriever=dict(
                    type='opencompass.openicl.icl_retriever.ZeroRetriever')),
            path='./data/math/math.json',
            reader_cfg=dict(
                input_columns=[
                    'problem',
                ],
                output_column='solution',
                test_range='[4400:4600]'),
            type='opencompass.datasets.MATHDataset'),
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
work_dir = './outputs/default/20241011_124504'
