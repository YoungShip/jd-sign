from pathlib import Path

text = Path('/home/nio/tmp-jd-sign-deploy/docs/index.html').read_text(encoding='utf-8')

assert 'const BATCH_KEY = \'jd_sign_batch_v1\';' in text, 'missing batch progress state key'
assert 'function getBatchState()' in text, 'missing batch state reader'
assert 'function continueBatchSign' in text, 'missing continue function'
assert 'document.addEventListener(\'visibilitychange\'' in text, 'missing return-to-page resume hook'
assert 'remaining.forEach((item, i) =>' not in text, 'old broken bulk-open loop still present'
assert 'i * 800' not in text, 'old timed bulk-open strategy still present'
assert 'continueBatchSign({ fromReturn: true });' in text, 'missing resume-continue flow on return'
print('ok')
