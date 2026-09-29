<template>
	<div class="flex p-1 bg-slate-100 rounded-xl border border-slate-200/60 shadow-inner">
		<button
			v-for="button in buttons"
			:key="button.key ?? button.label ?? button"
			class="py-2.5 transition-all rounded-lg flex-auto font-medium text-xs sm:text-sm text-center"
			:class="
				modelValue === (button.key ?? button.label ?? button)
					? 'bg-white shadow-sm text-slate-900 font-semibold'
					: 'text-slate-500 hover:text-slate-800'
			"
			@click="$emit('update:modelValue', button.key ?? button.label ?? button)"
		>
			{{ button.label ?? __(button) }}
		</button>
	</div>
</template>

<script setup>
const props = defineProps({
	buttons: {
		type: Array,
		required: true,
	},
	modelValue: {
		type: String,
	},
})

defineEmits(["update:modelValue"])
</script>
