from flask import Blueprint, render_template, request
import parser
import subprocess

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/', methods=['POST'])
def index_post():

     def isNoneOrEmpty(x):
          return x == None or x == ""

     program = request.form.get('program')

     matmul_size = request.form.get('matmul_size')
     tmm_tbmm_size = request.form.get('tmm_tbmm_size')
     conv2d_size = request.form.get('conv2d_size')
     map_size = request.form.get('map_size')
     custom_size = request.form.get('custom_size')

     autotuner = request.form.get('autotuner')
     tuner_threads = request.form.get('tuner_threads')
     tuner_generations = request.form.get('tuner_generations')
     pop_size = request.form.get('pop_size')
     number_of_elites = request.form.get('number_of_elites')

     map_to_blocks = request.form.get('map_to_blocks')
     map_to_threads = request.form.get('map_to_threads')
     tile = request.form.get('tile')
     unroll = request.form.get('unroll')

     load_from_cache = request.form.get('load_from_cache')
     store_to_cache = request.form.get('store_to_cache')
     use_shared_mem = request.form.get('use_shared_mem')
     unroll_copy_shared = request.form.get('unroll_copy_shared')
     use_read_only_cache = request.form.get('use_read_only_cache')
     match_lib_calls = request.form.get('match_lib_calls')
     fix_params = request.form.get('fix_params')
     outer_schedule_fusion_strategy = request.form.get('outer_schedule_fusion_strategy')

     intra_tile_fusion_strategy = request.form.get('intra_tile_fusion_strategy')

     # print(program, size, custom_size, autotuner, map_to_blocks, map_to_threads,
     # tile, unroll, load_from_cache, store_to_cache, use_shared_mem, unroll_copy_shared,
     # use_read_only_cache, match_lib_calls, fix_params, tuner_threads, tuner_generations, pop_size, number_of_elites, 
     # outer_schedule_fusion_strategy, intra_tile_fusion_strategy)

     base = "/opt/conda/anaconda/envs/tc_build/bin/python3 /Tvm-tc/tc/tc_bench.py --debug=True "
     program_part = "--prog={} ".format(program)

     if program == "matmul":  
          size_part = "--size {} ".format(matmul_size)
     elif program == "tmm" or program == "tbmm":
          size_part = "--size {} ".format(tmm_tbmm_size)
     elif program == "tmm" or program == "conv2d":
          size_part = "--size {} ".format(conv2d_size)
     elif program == "tmm" or program == "map":
          size_part = "--size {} ".format(map_size)
     else:
          size_part = "--size {} ".format(custom_size)

     autotuner_part = "" if isNoneOrEmpty(autotuner) else "--autotuner=True "
     tuner_threads_part = "" if isNoneOrEmpty(tuner_threads) else '--tuner_threads={} '.format(tuner_threads)
     tuner_generations_part = "" if isNoneOrEmpty(tuner_generations) else '--tuner_generations={} '.format(tuner_generations)
     pop_size_part = "" if isNoneOrEmpty(pop_size) else '--tuner_pop_size={} '.format(pop_size)
     number_of_elites_part = "" if isNoneOrEmpty(number_of_elites) else '--tuner_number_elites={} '.format(number_of_elites)
     load_from_cache_part = "--load_from_cache=False " if isNoneOrEmpty(load_from_cache) else "--load_from_cache=True "
     store_to_cache_part = "--store_to_cache=False " if isNoneOrEmpty(store_to_cache) else "--store_to_cache=True "
     use_shared_mem_part = "--useSharedMemory=False " if isNoneOrEmpty(use_shared_mem) else "--useSharedMemory=True "
     unroll_copy_shared_part = "--unrollCopyShared=False " if isNoneOrEmpty(unroll_copy_shared) else "--unrollCopyShared=True "
     use_read_only_cache_part = "--useReadOnlyCache=False " if isNoneOrEmpty(use_read_only_cache) else "--useReadOnlyCache=True "
     match_lib_calls_part = "--matchLibraryCalls=False " if isNoneOrEmpty(match_lib_calls) else "--matchLibraryCalls=True "
     fix_params_part = "--fixParametersBeforeScheduling=False " if isNoneOrEmpty(fix_params) else "--fixParametersBeforeScheduling=True "
     outer_schedule_fusion_strategy_part = "" if isNoneOrEmpty(outer_schedule_fusion_strategy) else "--outerScheduleFusionStrategy={} ".format(outer_schedule_fusion_strategy)
     intra_tile_fusion_strategy_part = "" if isNoneOrEmpty(intra_tile_fusion_strategy) else "--intraTileFusionStrategy={} ".format(intra_tile_fusion_strategy)
     map_to_blocks_part = "" if isNoneOrEmpty(map_to_blocks) else '--mapToBlocks {} '.format(map_to_blocks)
     map_to_threads_part = "" if isNoneOrEmpty(map_to_threads) else '--mapToThreads {} '.format(map_to_threads)
     tile_part = "" if isNoneOrEmpty(tile) else '--tile {} '.format(tile)
     unroll_part = "" if isNoneOrEmpty(unroll) else '--unroll={} '.format(unroll)

     # logfile_name = "/log.txt"

     command = base + program_part + size_part + autotuner_part + tuner_threads_part + tuner_generations_part + pop_size_part + number_of_elites_part + load_from_cache_part + store_to_cache_part + use_shared_mem_part  + unroll_copy_shared_part + use_read_only_cache_part + match_lib_calls_part + fix_params_part  + outer_schedule_fusion_strategy_part + intra_tile_fusion_strategy_part + map_to_blocks_part + map_to_threads_part + tile_part + unroll_part  #+ "&> {}".format(logfile_name)
     print(command)

     # echo = "echo '' > {}".format(logfile_name)
     # print(echo)

     # p = subprocess.Popen(echo, shell=True)
     # p.wait()

     p = subprocess.Popen(command, shell=True)
     (output, err) = p.communicate()
     p.wait()

     print(output)
     print(err)

     # output = parser.parse(logfile_name)

     # print("- - - -")
     # print(output)
     # print("- - - -")

     # return render_template('index.html', program=output[0])

     return render_template('index.html', program="Hi")