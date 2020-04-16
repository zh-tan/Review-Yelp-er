import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='food_1_star_large')


res = gpt2.generate(sess, run_name= 'food_1_star_large',
              length=130,
              prefix= "The chicken from KFC ", sample_delim = '<|endoftext|>', include_prefix=False, nsamples=1, return_as_list=True)
print(res)
